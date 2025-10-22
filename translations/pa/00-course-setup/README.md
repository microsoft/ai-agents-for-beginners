<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:36:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pa"
}
-->
# ਕੋਰਸ ਸੈਟਅਪ

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਇਸ ਕੋਰਸ ਦੇ ਕੋਡ ਨਮੂਨਿਆਂ ਨੂੰ ਕਿਵੇਂ ਚਲਾਇਆ ਜਾਵੇ।

## ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਜੁੜੋ ਅਤੇ ਮਦਦ ਪ੍ਰਾਪਤ ਕਰੋ

ਆਪਣਾ ਰਿਪੋ ਕਲੋਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ। ਇੱਥੇ ਤੁਹਾਨੂੰ ਸੈਟਅਪ ਵਿੱਚ ਮਦਦ, ਕੋਰਸ ਬਾਰੇ ਸਵਾਲਾਂ, ਜਾਂ ਹੋਰ ਸਿੱਖਣ ਵਾਲਿਆਂ ਨਾਲ ਜੁੜਨ ਦਾ ਮੌਕਾ ਮਿਲੇਗਾ।

## ਇਸ ਰਿਪੋ ਨੂੰ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ

ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ GitHub Repository ਨੂੰ ਕਲੋਨ ਜਾਂ ਫੋਰਕ ਕਰੋ। ਇਸ ਨਾਲ ਤੁਹਾਡੇ ਕੋਲ ਕੋਰਸ ਮਟੀਰੀਅਲ ਦਾ ਆਪਣਾ ਵਰਜਨ ਹੋਵੇਗਾ, ਜਿਸਨੂੰ ਤੁਸੀਂ ਚਲਾ ਸਕਦੇ ਹੋ, ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਸੋਧ ਸਕਦੇ ਹੋ!

ਇਹ <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">ਰਿਪੋ ਨੂੰ ਫੋਰਕ ਕਰਨ</a> ਲਈ ਲਿੰਕ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਇਸ ਕੋਰਸ ਦਾ ਆਪਣਾ ਫੋਰਕ ਕੀਤਾ ਵਰਜਨ ਹੇਠਾਂ ਦਿੱਤੇ ਲਿੰਕ ਵਿੱਚ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.pa.png)

### ਸ਼ੈਲੋ ਕਲੋਨ (ਵਰਕਸ਼ਾਪ / Codespaces ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ)

  >ਪੂਰਾ ਰਿਪੋ (~3 GB) ਡਾਊਨਲੋਡ ਕਰਨ ਸਮੇਂ ਵੱਡਾ ਹੋ ਸਕਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਸਿਰਫ ਵਰਕਸ਼ਾਪ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਰਹੇ ਹੋ ਜਾਂ ਸਿਰਫ ਕੁਝ ਪਾਠ ਫੋਲਡਰਾਂ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਸ਼ੈਲੋ ਕਲੋਨ (ਜਾਂ ਸਪਾਰਸ ਕਲੋਨ) ਇਤਿਹਾਸ ਅਤੇ/ਜਾਂ ਬਲੌਬਸ ਨੂੰ ਛੱਡ ਕੇ ਡਾਊਨਲੋਡ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ।

#### ਤੇਜ਼ ਸ਼ੈਲੋ ਕਲੋਨ — ਘੱਟ ਇਤਿਹਾਸ, ਸਾਰੇ ਫਾਈਲਾਂ

ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਵਿੱਚ `<your-username>` ਨੂੰ ਆਪਣੇ ਫੋਰਕ URL (ਜਾਂ ਉਪਸਟ੍ਰੀਮ URL) ਨਾਲ ਬਦਲੋ।

ਸਿਰਫ ਤਾਜ਼ਾ ਕਮਿਟ ਇਤਿਹਾਸ ਕਲੋਨ ਕਰਨ ਲਈ (ਛੋਟਾ ਡਾਊਨਲੋਡ):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

ਇੱਕ ਵਿਸ਼ੇਸ਼ ਸ਼ਾਖਾ ਕਲੋਨ ਕਰਨ ਲਈ:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### ਅੰਸ਼ਕ (ਸਪਾਰਸ) ਕਲੋਨ — ਘੱਟ ਬਲੌਬਸ + ਸਿਰਫ ਚੁਣੇ ਹੋਏ ਫੋਲਡਰ

ਇਹ ਅੰਸ਼ਕ ਕਲੋਨ ਅਤੇ ਸਪਾਰਸ-ਚੈਕਆਉਟ ਵਰਤਦਾ ਹੈ (Git 2.25+ ਦੀ ਲੋੜ ਹੈ ਅਤੇ ਅਧੁਨਿਕ Git ਨਾਲ ਅੰਸ਼ਕ ਕਲੋਨ ਸਹਾਇਤਾ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ ਹੈ):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

ਰਿਪੋ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ:

ਬੈਸ਼ ਲਈ:

```bash
cd ai-agents-for-beginners
```

ਪਾਵਰਸ਼ੈਲ ਲਈ:

```powershell
Set-Location ai-agents-for-beginners
```

ਫਿਰ ਉਹ ਫੋਲਡਰ ਚੁਣੋ ਜੋ ਤੁਹਾਨੂੰ ਚਾਹੀਦੇ ਹਨ (ਹੇਠਾਂ ਦਿੱਤੇ ਉਦਾਹਰਣ ਵਿੱਚ ਦੋ ਫੋਲਡਰ ਦਿਖਾਏ ਗਏ ਹਨ):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

ਕਲੋਨ ਕਰਨ ਅਤੇ ਫਾਈਲਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਜੇ ਤੁਹਾਨੂੰ ਸਿਰਫ ਫਾਈਲਾਂ ਦੀ ਲੋੜ ਹੈ ਅਤੇ ਜਗ੍ਹਾ ਖਾਲੀ ਕਰਨੀ ਹੈ (ਕੋਈ git ਇਤਿਹਾਸ ਨਹੀਂ), ਕਿਰਪਾ ਕਰਕੇ ਰਿਪੋਜ਼ਟਰੀ ਮੈਟਾਡੇਟਾ ਨੂੰ ਮਿਟਾ ਦਿਓ (💀ਅਣਰਿਵਰਸਿਬਲ — ਤੁਸੀਂ ਸਾਰੇ Git ਫੰਕਸ਼ਨਲਿਟੀ ਗੁਆ ਲਵੋਗੇ: ਕੋਈ ਕਮਿਟ, ਪੁਲ, ਪੁਸ਼ ਜਾਂ ਇਤਿਹਾਸ ਤੱਕ ਪਹੁੰਚ ਨਹੀਂ).

Linux/macOS ਲਈ:

```bash
rm -rf .git
```

Windows ਲਈ:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces ਵਰਤਣਾ (ਸਥਾਨਕ ਵੱਡੇ ਡਾਊਨਲੋਡ ਤੋਂ ਬਚਣ ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ)

- [GitHub UI](https://github.com/codespaces) ਰਾਹੀਂ ਇਸ ਰਿਪੋ ਲਈ ਨਵਾਂ Codespace ਬਣਾਓ।  

- ਨਵੇਂ ਬਣਾਏ ਗਏ ਕੋਡਸਪੇਸ ਦੇ ਟਰਮੀਨਲ ਵਿੱਚ, ਉਪਰੋਕਤ ਸ਼ੈਲੋ/ਸਪਾਰਸ ਕਲੋਨ ਕਮਾਂਡ ਚਲਾਓ ਤਾਂ ਜੋ ਸਿਰਫ ਉਹ ਪਾਠ ਫੋਲਡਰ ਜੋ ਤੁਹਾਨੂੰ ਚਾਹੀਦੇ ਹਨ, Codespace ਵਰਕਸਪੇਸ ਵਿੱਚ ਆ ਸਕਣ।
- ਵਿਕਲਪਿਕ: Codespaces ਵਿੱਚ ਕਲੋਨ ਕਰਨ ਤੋਂ ਬਾਅਦ, .git ਨੂੰ ਹਟਾਓ ਤਾਂ ਜੋ ਵਾਧੂ ਜਗ੍ਹਾ ਮੁੜ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾ ਸਕੇ (ਉਪਰੋਕਤ ਹਟਾਉਣ ਕਮਾਂਡ ਦੇਖੋ)।
- ਨੋਟ: ਜੇ ਤੁਸੀਂ ਰਿਪੋ ਨੂੰ ਸਿੱਧੇ Codespaces ਵਿੱਚ ਖੋਲ੍ਹਣਾ ਪਸੰਦ ਕਰਦੇ ਹੋ (ਬਿਨਾਂ ਵਾਧੂ ਕਲੋਨ), ਤਾਂ ਧਿਆਨ ਦਿਓ ਕਿ Codespaces devcontainer ਵਾਤਾਵਰਣ ਬਣਾਏਗਾ ਅਤੇ ਫਿਰ ਵੀ ਤੁਹਾਨੂੰ ਜ਼ਰੂਰਤ ਤੋਂ ਵੱਧ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ। ਇੱਕ ਤਾਜ਼ਾ Codespace ਵਿੱਚ ਇੱਕ ਸ਼ੈਲੋ ਕਾਪੀ ਕਲੋਨ ਕਰਨਾ ਡਿਸਕ ਦੀ ਵਰਤੋਂ 'ਤੇ ਵਧੇਰੇ ਕੰਟਰੋਲ ਦਿੰਦਾ ਹੈ।

#### ਟਿਪਸ

- ਜੇ ਤੁਸੀਂ ਸੋਧ/ਕਮਿਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਹਮੇਸ਼ਾ ਕਲੋਨ URL ਨੂੰ ਆਪਣੇ ਫੋਰਕ ਨਾਲ ਬਦਲੋ।
- ਜੇ ਤੁਹਾਨੂੰ ਬਾਅਦ ਵਿੱਚ ਹੋਰ ਇਤਿਹਾਸ ਜਾਂ ਫਾਈਲਾਂ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਉਹਨਾਂ ਨੂੰ ਫੈਚ ਕਰ ਸਕਦੇ ਹੋ ਜਾਂ ਸਪਾਰਸ-ਚੈਕਆਉਟ ਨੂੰ ਹੋਰ ਫੋਲਡਰ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਸਮਾਯੋਜਿਤ ਕਰ ਸਕਦੇ ਹੋ।

## ਕੋਡ ਚਲਾਉਣਾ

ਇਹ ਕੋਰਸ Jupyter Notebooks ਦੀ ਇੱਕ ਲੜੀ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਚਲਾ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ AI Agents ਬਣਾਉਣ ਦਾ ਹੱਥ-ਅਨੁਭਵ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ।

ਕੋਡ ਨਮੂਨੇ ਹੇਠਾਂ ਦਿੱਤੇ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਨੂੰ ਵਰਤਦੇ ਹਨ:

**GitHub ਖਾਤਾ ਲੋੜੀਂਦਾ ਹੈ - ਮੁਫ਼ਤ**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb) ਦੇ ਤੌਰ 'ਤੇ ਲੇਬਲ ਕੀਤਾ ਗਿਆ ਹੈ।
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb) ਦੇ ਤੌਰ 'ਤੇ ਲੇਬਲ ਕੀਤਾ ਗਿਆ ਹੈ।

**Azure Subscription ਲੋੜੀਂਦਾ ਹੈ**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb) ਦੇ ਤੌਰ 'ਤੇ ਲੇਬਲ ਕੀਤਾ ਗਿਆ ਹੈ।

ਅਸੀਂ ਤੁਹਾਨੂੰ ਤਿੰਨ ਕਿਸਮਾਂ ਦੇ ਉਦਾਹਰਣਾਂ ਨੂੰ ਅਜ਼ਮਾਉਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਤੁਸੀਂ ਵੇਖ ਸਕੋ ਕਿ ਤੁਹਾਡੇ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਕੌਣ ਹੈ।

ਤੁਹਾਡੇ ਦੁਆਰਾ ਚੁਣਿਆ ਗਿਆ ਵਿਕਲਪ ਇਹ ਨਿਰਧਾਰਤ ਕਰੇਗਾ ਕਿ ਹੇਠਾਂ ਦਿੱਤੇ ਸੈਟਅਪ ਕਦਮਾਂ ਵਿੱਚੋਂ ਕਿਹੜੇ ਤੁਹਾਨੂੰ ਪਾਲਣ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

## ਲੋੜਾਂ

- Python 3.12+
  - **NOTE**: ਜੇ ਤੁਹਾਡੇ ਕੋਲ Python3.12 ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਇਸਨੂੰ ਇੰਸਟਾਲ ਕਰੋ। ਫਿਰ python3.12 ਵਰਤ ਕੇ ਆਪਣਾ venv ਬਣਾਓ ਤਾਂ ਜੋ requirements.txt ਫਾਈਲ ਤੋਂ ਸਹੀ ਵਰਜਨ ਇੰਸਟਾਲ ਹੋ ਸਕਣ।
  
    >ਉਦਾਹਰਣ

    Python venv ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ:

    ``` bash
    python3 -m venv venv
    ```

    ਫਿਰ venv ਵਾਤਾਵਰਣ ਨੂੰ ਐਕਟੀਵੇਟ ਕਰੋ:

    macOS ਅਤੇ Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- GitHub ਖਾਤਾ - GitHub Models Marketplace ਤੱਕ ਪਹੁੰਚ ਲਈ
- Azure Subscription - Azure AI Foundry ਤੱਕ ਪਹੁੰਚ ਲਈ
- Azure AI Foundry ਖਾਤਾ - Azure AI Agent Service ਤੱਕ ਪਹੁੰਚ ਲਈ

ਅਸੀਂ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਰੂਟ ਵਿੱਚ ਇੱਕ `requirements.txt` ਫਾਈਲ ਸ਼ਾਮਲ ਕੀਤੀ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਲੋੜੀਂਦੇ Python ਪੈਕੇਜ ਹਨ ਜੋ ਕੋਡ ਨਮੂਨਿਆਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਲੋੜੀਂਦੇ ਹਨ।

ਤੁਸੀਂ ਇਸਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨੂੰ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਰੂਟ ਵਿੱਚ ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਚਲਾਕੇ ਇੰਸਟਾਲ ਕਰ ਸਕਦੇ ਹੋ:

```bash
pip install -r requirements.txt
```
ਅਸੀਂ ਕਿਸੇ ਵੀ ਟਕਰਾਅ ਅਤੇ ਸਮੱਸਿਆਵਾਂ ਤੋਂ ਬਚਣ ਲਈ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

## VSCode ਸੈਟਅਪ
ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ VSCode ਵਿੱਚ Python ਦਾ ਸਹੀ ਵਰਜਨ ਵਰਤ ਰਹੇ ਹੋ।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ਵਰਤ ਕੇ ਨਮੂਨਿਆਂ ਲਈ ਸੈਟਅਪ 

### ਕਦਮ 1: ਆਪਣਾ GitHub Personal Access Token (PAT) ਪ੍ਰਾਪਤ ਕਰੋ

ਇਹ ਕੋਰਸ GitHub Models Marketplace ਨੂੰ ਵਰਤਦਾ ਹੈ, ਜੋ ਤੁਹਾਨੂੰ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਤੱਕ ਮੁਫ਼ਤ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਤੁਸੀਂ AI Agents ਬਣਾਉਣ ਲਈ ਵਰਤੋਂਗੇ।

GitHub Models ਨੂੰ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

ਇਹ ਤੁਹਾਡੇ GitHub ਖਾਤੇ ਵਿੱਚ <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> 'ਤੇ ਜਾਕੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

ਕਿਰਪਾ ਕਰਕੇ [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ਦੀ ਪਾਲਣਾ ਕਰੋ ਜਦੋਂ ਤੁਸੀਂ ਆਪਣਾ ਟੋਕਨ ਬਣਾਉਂਦੇ ਹੋ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਸੀਂ ਟੋਕਨ ਨੂੰ ਸਿਰਫ ਉਹ ਅਧਿਕਾਰ ਦਿਓ ਜੋ ਇਸ ਕੋਰਸ ਵਿੱਚ ਕੋਡ ਨਮੂਨਿਆਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਲੋੜੀਂਦੇ ਹਨ।

1. **Developer settings** ਵਿੱਚ ਜਾਕੇ `Fine-grained tokens` ਵਿਕਲਪ ਚੁਣੋ।
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.pa.png)

    ਫਿਰ `Generate new token` ਚੁਣੋ।

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.pa.png)

2. ਆਪਣੇ ਟੋਕਨ ਲਈ ਇੱਕ ਵਰਣਨਾਤਮਕ ਨਾਮ ਦਿਓ ਜੋ ਇਸਦੇ ਉਦੇਸ਼ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੋਵੇ, ਤਾਂ ਜੋ ਇਸਨੂੰ ਬਾਅਦ ਵਿੱਚ ਆਸਾਨੀ ਨਾਲ ਪਛਾਣਿਆ ਜਾ ਸਕੇ।

    🔐 ਟੋਕਨ ਦੀ ਮਿਆਦ ਦੀ ਸਿਫਾਰਸ਼

    ਸਿਫਾਰਸ਼ ਕੀਤੀ ਮਿਆਦ: 30 ਦਿਨ
    ਜੇ ਤੁਸੀਂ ਹੋਰ ਸੁਰੱਖਿਅਤ ਪਹੁੰਚ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਛੋਟੀ ਮਿਆਦ—ਜਿਵੇਂ ਕਿ 7 ਦਿਨ 🛡️ ਚੁਣ ਸਕਦੇ ਹੋ।
    ਇਹ ਇੱਕ ਵਧੀਆ ਤਰੀਕਾ ਹੈ ਆਪਣਾ ਨਿੱਜੀ ਟਾਰਗਟ ਸੈਟ ਕਰਨ ਦਾ ਅਤੇ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਦਾ ਜਦੋਂ ਤੁਹਾਡਾ ਸਿੱਖਣ ਦਾ ਜ਼ੋਰ ਉੱਚਾ ਹੋਵੇ 🚀।

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.pa.png)

3. ਟੋਕਨ ਦੀ ਸਕੋਪ ਨੂੰ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਫੋਰਕ ਤੱਕ ਸੀਮਿਤ ਕਰੋ।

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.pa.png)

4. ਟੋਕਨ ਦੇ ਅਧਿਕਾਰਾਂ ਨੂੰ ਸੀਮਿਤ ਕਰੋ: **Permissions** ਦੇ ਅਧੀਨ, **Account** ਟੈਬ 'ਤੇ ਕਲਿੱਕ ਕਰੋ, ਅਤੇ "+ Add permissions" ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਇੱਕ ਡ੍ਰਾਪਡਾਊਨ ਪ੍ਰਗਟ ਹੋਵੇਗਾ। ਕਿਰਪਾ ਕਰਕੇ **Models** ਦੀ ਖੋਜ ਕਰੋ ਅਤੇ ਇਸਦੇ ਲਈ ਬਾਕਸ ਚੈੱਕ ਕਰੋ।
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.pa.png)

5. ਟੋਕਨ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਲੋੜੀਂਦੇ ਅਧਿਕਾਰਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ। ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.pa.png)

6. ਟੋਕਨ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਟੋਕਨ ਨੂੰ ਸੁਰੱਖਿਅਤ ਥਾਂ ਜਿਵੇਂ ਕਿ ਪਾਸਵਰਡ ਮੈਨੇਜਰ ਵਾਲਟ ਵਿੱਚ ਸਟੋਰ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ, ਕਿਉਂਕਿ ਇਹ ਟੋਕਨ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਦੁਬਾਰਾ ਨਹੀਂ ਦਿਖਾਇਆ ਜਾਵੇਗਾ। ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.pa.png)

ਆਪਣੇ ਨਵੇਂ ਬਣਾਏ ਟੋਕਨ ਨੂੰ ਕਾਪੀ ਕਰੋ। ਹੁਣ ਤੁਸੀਂ ਇਸਨੂੰ ਇਸ ਕੋਰਸ ਵਿੱਚ ਸ਼ਾਮਲ `.env` ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋਗੇ।

### ਕਦਮ 2: ਆਪਣੀ `.env` ਫਾਈਲ ਬਣਾਓ

ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨੂੰ ਚਲਾਕੇ `.env` ਫਾਈਲ ਬਣਾਓ।

```bash
cp .env.example .env
```

ਇਹ ਉਦਾਹਰਣ ਫਾਈਲ ਨੂੰ ਕਾਪੀ ਕਰੇਗਾ ਅਤੇ `.env` ਤੁਹਾਡੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਬਣਾਏਗਾ, ਜਿੱਥੇ ਤੁਸੀਂ ਵਾਤਾਵਰਣ ਚਰਾਂ ਦੀਆਂ ਕੀਮਤਾਂ ਭਰਦੇ ਹੋ।

ਆਪਣੇ ਟੋਕਨ ਨੂੰ ਕਾਪੀ ਕਰਕੇ, `.env` ਫਾਈਲ ਨੂੰ ਆਪਣੇ ਮਨਪਸੰਦ ਟੈਕਸਟ ਐਡੀਟਰ ਵਿੱਚ ਖੋਲ੍ਹੋ ਅਤੇ ਆਪਣੇ ਟੋਕਨ ਨੂੰ `GITHUB_TOKEN` ਫੀਲਡ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.pa.png)

ਹੁਣ ਤੁਸੀਂ ਇਸ ਕੋਰਸ ਦੇ ਕੋਡ ਨਮੂਨਿਆਂ ਨੂੰ ਚਲਾ ਸਕਦੇ ਹੋ।

## Azure AI Foundry ਅਤੇ Azure AI Agent Service ਵਰਤ ਕੇ ਨਮੂਨਿਆਂ ਲਈ ਸੈਟਅਪ

### ਕਦਮ 1: ਆਪਣਾ Azure ਪ੍ਰੋਜੈਕਟ ਐਂਡਪੌਇੰਟ ਪ੍ਰਾਪਤ ਕਰੋ

Azure AI Foundry ਵਿੱਚ ਹੱਬ ਅਤੇ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਦੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

ਜਦੋਂ ਤੁਸੀਂ ਆਪਣਾ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਲਈ ਕਨੈਕਸ਼ਨ ਸਟ੍ਰਿੰਗ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

ਇਹ Azure AI Foundry ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੇ **Overview** ਪੇਜ 'ਤੇ ਜਾਕੇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.pa.png)

### ਕਦਮ 2: ਆਪਣੀ `.env` ਫਾਈਲ ਬਣਾਓ

ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨੂੰ ਚਲਾਕੇ `.env` ਫਾਈਲ ਬਣਾਓ।

```bash
cp .env.example .env
```

ਇਹ ਉਦਾਹਰਣ ਫਾਈਲ ਨੂੰ ਕਾਪੀ ਕਰੇਗਾ ਅਤੇ `.env` ਤੁਹਾਡੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਬਣਾਏਗਾ, ਜਿੱਥੇ ਤੁਸੀਂ ਵਾਤਾਵਰਣ ਚਰਾਂ ਦੀਆਂ ਕੀਮਤਾਂ ਭਰਦੇ ਹੋ।

ਆਪਣੇ ਟੋਕਨ ਨੂੰ ਕਾਪੀ ਕਰਕੇ, `.env` ਫਾਈਲ ਨੂੰ ਆਪਣੇ ਮਨਪਸੰਦ ਟੈਕਸਟ ਐਡੀਟਰ ਵਿੱਚ ਖੋਲ੍ਹੋ ਅਤੇ ਆਪਣੇ ਟੋਕਨ ਨੂੰ `PROJECT_ENDPOINT` ਫੀਲਡ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।

### ਕਦਮ 3: Azure ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ

ਸੁਰੱਖਿਆ ਦੇ ਵਧੀਆ ਅਭਿਆਸ ਦੇ ਤੌਰ 'ਤੇ, ਅਸੀਂ [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵਰਤ ਕੇ Microsoft Entra ID ਨਾਲ Azure OpenAI ਵਿੱਚ ਪ੍ਰਮਾਣਿਕਤਾ ਪ੍ਰਾਪਤ ਕਰਾਂਗੇ।

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ `az login --use-device-code` ਚਲਾਕੇ ਆਪਣੇ Azure ਖਾਤੇ ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

ਜਦੋਂ ਤੁਸੀਂ ਲੌਗਇਨ ਕਰ ਲੈਂਦੇ ਹੋ, ਟਰਮੀਨਲ ਵਿੱਚ ਆਪਣੀ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।

## ਵਾਧੂ ਵਾਤਾਵਰਣ ਚਰ - Azure Search ਅਤੇ Azure OpenAI 

Agentic RAG Lesson - Lesson 5 ਲਈ - ਕੁਝ ਨਮੂਨੇ Azure Search ਅਤੇ Azure OpenAI ਵਰਤਦੇ ਹਨ।

ਜੇ ਤੁਸੀਂ ਇਹ ਨਮੂਨੇ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਹ
ਜੇ ਤੁਹਾਨੂੰ ਇਸ ਸੈਟਅੱਪ ਨੂੰ ਚਲਾਉਣ ਵਿੱਚ ਕੋਈ ਸਮੱਸਿਆ ਆਉਂਦੀ ਹੈ, ਤਾਂ ਸਾਡੇ <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਜਾਓ ਜਾਂ <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">ਇੱਕ ਸਮੱਸਿਆ ਬਣਾਓ</a>।

## ਅਗਲਾ ਪਾਠ

ਤੁਸੀਂ ਹੁਣ ਇਸ ਕੋਰਸ ਲਈ ਕੋਡ ਚਲਾਉਣ ਲਈ ਤਿਆਰ ਹੋ। AI ਏਜੰਟਸ ਦੀ ਦੁਨੀਆ ਬਾਰੇ ਹੋਰ ਸਿੱਖਣ ਦਾ ਅਨੰਦ ਮਾਣੋ!

[AI ਏਜੰਟਸ ਅਤੇ ਏਜੰਟ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦਾ ਪਰਿਚਯ](../01-intro-to-ai-agents/README.md)

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।