# Azure Troubleshooting Guide for Trainers

This guide documents Azure-specific issues encountered during trainer prep and how to resolve them.

---

## 🔐 RBAC Permissions

### Issue: `403 - AuthenticationTypeDisabled`

**Full Error:**
```
Error code: 403 - {'error': {'code': 'AuthenticationTypeDisabled', 'message': 'Key based authentication is disabled for this resource.'}}
```

**Root Cause:**  
Your Azure OpenAI resource has key-based authentication disabled by policy. You must use Microsoft Entra ID (formerly Azure AD) authentication.

**Solution:**

1. **Use InteractiveBrowserCredential** in notebooks:
   ```python
   from azure.identity import InteractiveBrowserCredential
   from agent_framework.azure import AzureOpenAIChatClient
   
   credential = InteractiveBrowserCredential()
   openai_chat_client = AzureOpenAIChatClient(
       azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
       credential=credential,  # Pass credential directly
       azure_deployment=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
       api_version=os.environ.get("AZURE_OPENAI_API_VERSION")
   )
   ```

2. **Ensure you have the required role:**  
   You need **"Cognitive Services OpenAI User"** role assigned on your Azure OpenAI resource.
   
   For **Azure AI Foundry projects** (Lesson 5 RAG), you need:
   - **"Azure AI User"** role on the Azure AI Foundry **PROJECT** (not the Hub)
   - This includes the required data actions: 
     - `Microsoft.CognitiveServices/accounts/AIServices/assets/write` (for file upload)
     - `Microsoft.CognitiveServices/accounts/AIServices/agents/write` (for agent creation)
     - `agents/*/read`, `agents/*/action`, `agents/*/delete`
   
   **⚠️ IMPORTANT: Hub vs Project**
   - **Hub**: Parent workspace (e.g., `myFoundryHub`) - permissions here do NOT grant project access
   - **Project**: Child workspace (e.g., `proj-default`) - **this is where you need the role**
   - Always assign permissions to the **Project**, not the Hub!
   
   **To assign the role via Azure AI Foundry Portal (RECOMMENDED):**
   1. Navigate to [Azure AI Foundry](https://ai.azure.com)
   2. Select your **PROJECT** from the list (not the Hub - look for names like `proj-default`)
   3. Click on the **Agents** page in the left navigation
   4. If you see the error "Your principal is missing the Azure AI User role", click the **"Fix me"** button
      - This will automatically assign the Azure AI User role to your account
   5. **Alternative manual method:** Click **Settings** (left sidebar) → **Permissions** tab → **+ Add member** → Select role: **Azure AI User**
   6. Wait 5-10 minutes for the role to propagate
   
   **Alternative: PowerShell (requires User Access Administrator role):**
   ```powershell
   # Get your user ID
   $userId = (Get-AzADUser -UserPrincipalName "your.email@domain.com").Id
   
   # Get your project (update resource group and project name)
   $project = Get-AzMLWorkspace -ResourceGroupName "YOUR_RESOURCE_GROUP" -Name "YOUR_PROJECT_NAME"
   
   # Assign the Azure AI User role (not Azure AI Developer)
   New-AzRoleAssignment -ObjectId $userId -RoleDefinitionName "Azure AI User" -Scope $project.Id
   ```
   
   **Note:** Role assignments may take 5-10 minutes to propagate. You may need to clear your credential cache or restart your Python kernel after assignment.

3. **⚠️ CRITICAL: Remove AZURE_OPENAI_API_KEY from environment**  
   If `AZURE_OPENAI_API_KEY` is set in your `.env` file, the SDK will prefer API key authentication over Microsoft Entra ID, causing the 403 error.
   
   **Fix:**
   - Remove `AZURE_OPENAI_API_KEY` from your `.env` file
   - Restart your Jupyter kernel
   - Recreate the `AzureOpenAIChatClient` instance
   
   **Verify:**
   ```python
   import os
   print(f"API Key set: {os.environ.get('AZURE_OPENAI_API_KEY') is not None}")
   # Should print: API Key set: False
   ```

---

### Issue: Cannot Create Agent - "Azure AI User" Role Assignment Option is Disabled

**Symptoms:**
- When trying to create an agent in Azure AI Foundry (v2), you see an error message
- The error indicates you need the "Azure AI User" role
- When you navigate to Settings → Permissions to assign the role, the **"Azure AI User" option is disabled/greyed out**
- You cannot click or select the role to assign it to yourself

**Root Cause:**  
You don't have sufficient permissions to assign roles on the Azure AI Foundry project. Only users with **Owner** or **User Access Administrator** roles can assign RBAC permissions to others (or themselves).

**Solution Options:**

**Option 1: Use the "Fix me" Button (EASIEST - RECOMMENDED)**

1. Navigate to [Azure AI Foundry](https://ai.azure.com)
2. Select your **PROJECT** (e.g., `proj-default`) - **NOT the Hub**
3. Click on **Agents** in the left navigation
4. If you see the banner **"Your principal is missing the Azure AI User role"**, click the **"Fix me"** button
   - This button has special permissions and can often assign the role even when manual assignment is disabled
   - The role will be automatically assigned to your account
5. Wait 5-10 minutes for the role to propagate
6. Refresh the page and try creating an agent again

**Option 2: Contact Your Azure Administrator**

If the "Fix me" button doesn't work or isn't available, you need someone with elevated permissions to assign the role:

1. Identify who has **Owner** or **User Access Administrator** role on your Azure subscription or project
   - For this course: Contact **David Yu** (tenant admin) or **Chad Toney** (see Emergency Contacts section below)
   - For your organization: Contact your Azure subscription administrator

2. Request they assign you the **"Azure AI User"** role on the **PROJECT** (not the Hub)

3. They can assign it via:
   
   **Azure AI Foundry Portal:**
   - Go to [Azure AI Foundry](https://ai.azure.com) → Select the PROJECT
   - Click **Settings** → **Permissions** → **+ Add member**
   - Search for your user email
   - Select role: **Azure AI User**
   - Click **Add**
   
   **OR Azure Portal:**
   - Go to [Azure Portal](https://portal.azure.com)
   - Navigate to the Azure AI Foundry project resource
   - Click **Access control (IAM)** → **+ Add** → **Add role assignment**
   - Select role: **Azure AI User**
   - Select your user account
   - Click **Review + assign**
   
   **OR PowerShell:**
   ```powershell
   # Get user ID
   $userId = (Get-AzADUser -UserPrincipalName "user.email@domain.com").Id
   
   # Get project resource
   $project = Get-AzMLWorkspace -ResourceGroupName "YOUR_RESOURCE_GROUP" -Name "YOUR_PROJECT_NAME"
   
   # Assign Azure AI User role
   New-AzRoleAssignment -ObjectId $userId -RoleDefinitionName "Azure AI User" -Scope $project.Id
   ```

**Option 3: Use GitHub Models as a Workaround (TEMPORARY)**

While waiting for role assignment, you can use the free GitHub Models to complete the lessons:

1. Follow the [GitHub Models setup instructions](../00-course-setup/README.md#set-up-for-samples-using-github-models) 
2. Use the `*-semantic-kernel.ipynb` or `*-autogen.ipynb` notebooks instead of `*-azureaiagent.ipynb`
3. These don't require Azure AI Foundry and work with just a GitHub account
4. Once you get the "Azure AI User" role, you can return to the Azure AI Agent Service examples

**Verification:**

After role assignment, verify it worked:

1. Wait 5-10 minutes for Azure RBAC propagation
2. Navigate to [Azure AI Foundry](https://ai.azure.com) → Your PROJECT → **Agents**
3. Try creating a new agent
4. You should now be able to create agents without errors

**Common Mistakes:**
- ❌ Trying to assign the role to yourself when you don't have Owner/User Access Administrator permissions
- ❌ Assigning the role on the **Hub** instead of the **Project**
- ❌ Not waiting 5-10 minutes after role assignment for propagation
- ✅ Using the "Fix me" button in Azure AI Foundry (it has special permissions)
- ✅ Contacting an administrator with proper permissions to assign the role
- ✅ Ensuring the role is assigned on the **Project**, not the Hub

---

### Issue: `PermissionDenied` on Azure AI Foundry (Lesson 5 RAG)

**Full Error:**
```
ClientAuthenticationError: (PermissionDenied) The principal `user@domain.com` lacks the required data action `Microsoft.CognitiveServices/accounts/AIServices/assets/write` to perform `POST /api/projects/{projectName}/files` operation.
```

**Root Cause:**  
You don't have the required role on your Azure AI Foundry **PROJECT** to upload files and create vector stores.

**Solution:**

1. **Assign "Azure AI User" role on your PROJECT (not Hub):**
   - Navigate to [Azure AI Foundry](https://ai.azure.com)
   - Select your **PROJECT** (e.g., `proj-default`) - **NOT the Hub**
   - Click on **Agents** in the left navigation
   - If you see "Your principal is missing the Azure AI User role", click **"Fix me"**
   - This automatically assigns the role to your account
   
   **Alternative manual method:**
   - Click **Settings** → **Permissions**
   - Click **+ Add member**
   - Search for your user email
   - Select role: **Azure AI User**
   - Click **Add**
   
   **Common mistake:** Assigning the role to the Hub instead of the Project won't work!

2. **Wait 5-10 minutes** for the role assignment to propagate

3. **Use `DefaultAzureCredential` for authentication:**
   ```python
   from azure.identity.aio import DefaultAzureCredential
   from agent_framework.azure import AzureAIAgentClient
   
   credential = DefaultAzureCredential()
   chat_client = AzureAIAgentClient(credential=credential)
   ```

4. **Verify the fix:**
   - Re-run the notebook cell that uploads files
   - You should now see: "Uploaded file, file ID: file-..."

**Note:** `DefaultAzureCredential` works better than `AzureCliCredential` on Windows due to DLL issues with Azure CLI.

---

### Issue: Lesson 5 SDK Confusion - `AgentsClient` vs `AIProjectClient`

**Symptom:**
```python
AttributeError: 'AgentsOperations' object has no attribute 'files'
```

**Root Cause:**  
There are two different client types for Azure AI Agents, and the docs can be confusing:
- `AIProjectClient` from `azure-ai-projects` - for managing agents (create/list/delete agents)
- `AgentsClient` from `azure-ai-agents` - for agent conversations (files, threads, messages, runs)

**Solution for Lesson 5 RAG:**

Use `AgentsClient` directly from `azure.ai.agents`:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FilePurpose, FileSearchTool, ListSortOrder

agents_client = AgentsClient(
    endpoint=os.environ.get("PROJECT_ENDPOINT") or os.environ.get("AZURE_AI_PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential(),
)

# Now you have access to:
# - agents_client.files.upload_and_poll()
# - agents_client.vector_stores.create_and_poll()
# - agents_client.create_agent()
# - agents_client.threads.create()
# - agents_client.messages.create()
# - agents_client.runs.create_and_process()
```

**Don't use:**
```python
# ❌ Wrong - AIProjectClient.agents is for management operations only
from azure.ai.projects import AIProjectClient
project_client = AIProjectClient(...)
project_client.agents.files  # This doesn't exist!
```

**Environment Variables Needed:**
- `PROJECT_ENDPOINT` or `AZURE_AI_PROJECT_ENDPOINT` - Your Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., "gpt-4o-mini")

---

### Issue: `401 - PermissionDenied`

**Full Error:**
```
Error code: 401 - {'error': {'code': 'PermissionDenied', 'message': 'The principal lacks the required data action Microsoft.CognitiveServices/accounts/OpenAI/deployments/chat/completions/action'}}
```

**Root Cause:**  
You're successfully authenticating (getting a token), but you don't have the Azure RBAC role required to call the OpenAI API.

**Solution:**

**Option 1: Request Direct Role Assignment (Recommended)**

Contact David Yu (tenant admin) to assign the role.

**✅ Solution Used for February 2025 Training:**

David Yu assigned "Cognitive Services OpenAI User" role to the entire trainer group **RockstarAIPresentersFeb2025**, which includes all 12 trainers. This is the recommended approach for training events.

```powershell
# Command David Yu used (group-based assignment):
$groupObjectId = (Get-AzADGroup -DisplayName "RockstarAIPresentersFeb2025").Id
$resourceGroup = "your-resource-group"
$accountName = "your-openai-account"

$cognitiveAccount = Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $accountName

New-AzRoleAssignment `
    -ObjectId $groupObjectId `
    -RoleDefinitionName "Cognitive Services OpenAI User" `
    -Scope $cognitiveAccount.Id
```

**Alternative (individual user assignment):**
```powershell
$userEmail = "your.email@MngEnvMCAP295748.onmicrosoft.com"
$resourceGroup = "your-resource-group"
$accountName = "your-openai-account"

$cognitiveAccount = Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $accountName

New-AzRoleAssignment `
    -SignInName $userEmail `
    -RoleDefinitionName "Cognitive Services OpenAI User" `
    -Scope $cognitiveAccount.Id
```

**Option 2: Self-Service via PIM (If Enabled)**

If David Yu has enabled PIM (Privileged Identity Management):

1. Go to **Azure Portal** → **PIM**
2. Navigate to **My Roles** → **Azure Resources**
3. Find **Owner** or **User Access Administrator** role
4. Click **Activate** (may require approval)
5. Once active, assign yourself "Cognitive Services OpenAI User":
   ```powershell
   New-AzRoleAssignment `
       -SignInName "your.email@MngEnvMCAP295748.onmicrosoft.com" `
       -RoleDefinitionName "Cognitive Services OpenAI User" `
       -Scope "/subscriptions/SUB-ID/resourceGroups/RG-NAME/providers/Microsoft.CognitiveServices/accounts/ACCOUNT-NAME"
   ```

**Important:** Wait 5-10 minutes after role assignment for Azure RBAC propagation.

---

### Issue: PIM Role Activation Not Working

**Symptoms:**
- You activated a PIM role (like "User Administrator")
- Role assignment commands still return `Forbidden` error

**Root Cause:**  
**Entra ID roles** (like User Administrator) ≠ **Azure RBAC roles** (like Owner, Contributor)

- **Entra ID roles** manage users, groups, applications
- **Azure RBAC roles** manage Azure resources

**Solution:**  
You need an **Azure RBAC role** on the resource, not an Entra ID role:

- **"Owner"** (full access + role assignment)
- **"User Access Administrator"** (can assign roles)
- **"Cognitive Services OpenAI User"** (minimum required)

Contact David Yu to assign an Azure RBAC role.

---

## 🔍 Verifying Your Setup

### Check Azure Connectivity

```powershell
# Connect to Azure
Connect-AzAccount -UseDeviceAuthentication

# List your subscriptions
Get-AzSubscription

# Check role assignments
Get-AzRoleAssignment -SignInName "your.email@MngEnvMCAP295748.onmicrosoft.com" | 
    Select-Object RoleDefinitionName, Scope | 
    Format-Table -AutoSize
```

### Test Azure OpenAI Access

```python
from azure.identity import InteractiveBrowserCredential
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print('Testing Azure OpenAI connection...')
credential = InteractiveBrowserCredential()
token = credential.get_token('https://cognitiveservices.azure.com/.default').token
print('✓ Token obtained')

client = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    azure_ad_token=token
)

try:
    response = client.chat.completions.create(
        model=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME'),
        messages=[{'role': 'user', 'content': 'Say hello'}],
        max_tokens=10
    )
    print('✓ SUCCESS! Azure OpenAI is working!')
    print(f'Response: {response.choices[0].message.content}')
except Exception as e:
    print(f'✗ FAILED: {e}')
```

---

## � Package Compatibility Issues

### Issue: Lesson 5 - `agent-framework-azure-ai` MCP Conflict

**Symptoms:**
```python
AttributeError: module 'mcp.types' has no attribute 'ToolUseContent'
```

**Root Cause:**  
Incompatibility between `agent-framework-azure-ai` (required for Lesson 5 RAG) and `mcp[cli]` package versions.

**Current Status:** **KNOWN ISSUE** (as of January 2026)

**Workaround Options:**

1. **Skip Lesson 5 for now** - Focus on Lessons 12-13 (your teaching assignments)
2. **Use alternative RAG implementation** - ChromaDB version (`05-python-chromadb.ipynb`)
3. **Wait for package updates** - Monitor agent-framework releases

**Azure AI Foundry Requirements for Lesson 5:**
- `AZURE_AI_PROJECT_ENDPOINT` - Your Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o-mini)
- Azure AI Foundry Hub & Project created
- Vector store capabilities enabled

**Recommended Path:**  
Given the dependency conflict and complexity, prioritize **Lessons 12-13** (Context Engineering & Agent Memory) for training prep. Lesson 5 RAG concepts can be covered conceptually with slides/demos without hands-on lab.

---

## �🛠️ Azure CLI Issues

### Issue: Azure CLI DLL Import Errors

**Error:**
```
ImportError: DLL load failed while importing win32file
```

**Solution:**  
Use **Azure PowerShell** instead:

```powershell
# Install Azure PowerShell (if not installed)
Install-Module -Name Az -Repository PSGallery -Force

# Connect to Azure
Connect-AzAccount -UseDeviceAuthentication
```

Azure PowerShell provides equivalent functionality and is more reliable on Windows.

---

## 🌐 Common Environment Issues

### Issue: Wrong API Version

**Symptoms:**
- API calls fail with version-related errors
- Deployments not found

**Solution:**  
Update `AZURE_OPENAI_API_VERSION` in `.env`:

```env
AZURE_OPENAI_API_VERSION="2025-01-01-preview"
```

Latest stable versions:
- `2025-01-01-preview` (recommended)
- `2024-12-01-preview`
- `2024-10-21`

### Issue: Deployment Name Mismatch

**Symptoms:**
- `DeploymentNotFound` errors

**Solution:**  
Verify deployment name matches exactly:

```powershell
# List deployments in your Azure OpenAI account
az cognitiveservices account deployment list \
    --name "your-openai-account" \
    --resource-group "your-resource-group"
```

Update `.env` with the exact deployment name:

```env
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"  # Must match exactly
```

---

## 📋 Pre-Training Checklist

Before the training event, verify:

- [ ] Azure OpenAI resource created and accessible
- [ ] `Cognitive Services OpenAI User` role assigned
- [ ] Authentication working (InteractiveBrowserCredential)
- [ ] `.env` configured with correct endpoints and deployment names
- [ ] Test notebook executes successfully (Lesson 1)
- [ ] Azure AI Search created (if teaching Lessons 5 or 13)
- [ ] Backup plan if Azure has issues (GitHub Models credentials)

---

## 🆘 Emergency Contacts

### Azure Permission Issues
- **David Yu** (tenant owner) - Can assign Azure RBAC roles

### Technical Support
- **Chad Toney** - chad.toney@MngEnvMCAP295748.onmicrosoft.com
- **Trainer Discord Channel** - For real-time help

### Microsoft Support
- **Azure Support Portal** - For Azure resource issues
- **Azure AI Discord** - https://aka.ms/ai-agents/discord

---

## 📚 Useful Documentation

- [Keyless Authentication with Azure AI](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=python%2Cazure-cli)
- [Azure RBAC Overview](https://learn.microsoft.com/azure/role-based-access-control/overview)
- [Azure OpenAI Service RBAC](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control)
- [Privileged Identity Management (PIM)](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/)

---

**Last Updated:** January 6, 2026  
**Maintained by:** Chad Toney
