# Context Engineering using Azure AI Foundry UI (No Code Required)

This guide shows how to implement context engineering with agent scratchpad capabilities using **only** the Azure AI Foundry graphical interface - no programming required!

> **⚡ Quick Start:** This is a GUI-first approach that builds on the Travel Planning Agent from Lesson 7.
> If you haven't completed Lesson 7, start there first to create the base agent.

## 📋 What You'll Build

A vacation planning agent that:
- ✅ Remembers user preferences across conversations (budget, destinations, activities)
- ✅ Maintains a scratchpad of completed tasks
- ✅ Retrieves context before making recommendations
- ✅ Persists information beyond a single conversation

## 🎯 Prerequisites

- ✅ Azure AI Foundry access ([https://ai.azure.com](https://ai.azure.com))
- ✅ Completed **Lesson 7** Travel Planning Agent (or any existing agent in Azure AI Foundry)
- ✅ Basic understanding of context engineering concepts (from Lesson 12 README)

## 🚀 Implementation Steps

### Step 1: Navigate to Your Agent

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your **Project**
3. Click **Agents** in the left navigation
4. Select your **Travel Planning Agent** from Lesson 7 (or create a new one)

### Step 2: Add File Upload Capability

The agent needs to read/write to a scratchpad file. We'll use the **File Search** tool:

1. In your agent's configuration, scroll to **Tools**
2. Enable **File Search**
3. Click **Save**

> **Note:** File Search allows the agent to read uploaded files. We'll use it to read our scratchpad.

### Step 3: Create the Scratchpad File

1. Create a new file locally called `vacation_scratchpad.md`
2. Add this initial content:

```markdown
# Vacation Planning Agent Scratchpad

## User Preferences
<!-- Agent will add preferences here -->

## Completed Tasks
<!-- Agent will record completed work here -->

## Notes
<!-- Agent can add contextual notes here -->
```

3. Save the file

### Step 4: Upload Scratchpad to Agent

1. In your agent's interface, look for the **Files** or **Knowledge** section
2. Click **Upload file**
3. Select your `vacation_scratchpad.md` file
4. Wait for upload to complete

> **💡 Tip:** Some interfaces call this "Vector Store" or "Knowledge Base" - same concept!

### Step 5: Update Agent Instructions

Update your agent's system instructions to include scratchpad management:

```
You are a helpful vacation planning assistant.

SCRATCHPAD MANAGEMENT (CRITICAL):
1. ALWAYS check the vacation_scratchpad.md file at the START of each conversation
2. When a user mentions preferences (budget, destinations, activities), ADD them to the "User Preferences" section
3. When you complete a task (create itinerary, book something), ADD it to "Completed Tasks" section
4. BEFORE making recommendations, READ the scratchpad to personalize your response

SCRATCHPAD FORMAT:
- Add preferences as bullet points under "## User Preferences"
- Add completed tasks with timestamps under "## Completed Tasks"
- Add any important context under "## Notes"

EXAMPLE SCRATCHPAD UPDATES:
When user says "I love beach destinations":
- Add: "- Prefers beach destinations with warm weather"

When user says "Budget is $3000 per person":
- Add: "- Budget: $3000 per person for a week-long trip"

When you create an itinerary:
- Add: "- [2026-02-04] Created 7-day Bali itinerary with beach activities"

PLANNING WORKFLOW:
1. Check scratchpad for existing preferences
2. Ask clarifying questions if needed
3. Create detailed, personalized recommendations
4. Update scratchpad with new information
5. Update scratchpad with completed tasks

Be proactive about checking and updating the scratchpad!
```

### Step 6: Test the Agent - First Conversation

Start a new conversation:

**User:** "I'm planning a vacation. Can you help?"

**Expected Behavior:**
- Agent checks the scratchpad
- Asks about your preferences
- Takes notes in the scratchpad

**User:** "I love beach destinations and my budget is around $3000 per person for a week."

**Expected Behavior:**
- Agent acknowledges preferences
- Updates scratchpad with this information
- Asks follow-up questions

**User:** "Please create an itinerary for Bali."

**Expected Behavior:**
- Agent creates detailed itinerary
- Marks task as complete in scratchpad

### Step 7: Download and Review Scratchpad

1. In the agent interface, find the uploaded `vacation_scratchpad.md` file
2. Download it to see what the agent recorded
3. Open in a text editor

You should see your preferences and completed tasks listed!

### Step 8: Test Persistence - New Conversation

1. **Start a BRAND NEW conversation** (use the "New chat" or "+" button)
2. Ask: "Hi! Can you help me plan a trip?"

**Expected Behavior:**
- Agent checks the scratchpad
- Agent says something like: "I see you prefer beach destinations and have a budget of $3000 per person..."
- Agent uses past preferences to make recommendations

**This proves the memory persists across conversations!**

### Step 9: Change Preferences

**User:** "Actually, I'd prefer mountain destinations this time."

**Expected Behavior:**
- Agent updates scratchpad with new preference
- Creates recommendations for mountains while remembering budget constraint

### Step 10: Review Final Scratchpad

Download the scratchpad again and review:
- Original preferences
- New preferences
- All completed tasks with timestamps
- Any notes the agent made

## 🎓 What You've Learned

### Context Engineering Concepts Applied:

1. **Persistent Memory**: Scratchpad file stores information beyond a single session
2. **Context Retrieval**: Agent reads scratchpad before responding
3. **Context Writing**: Agent updates scratchpad with new information
4. **Task Tracking**: Completed work is recorded
5. **User Isolation**: Each user could have their own scratchpad file (in multi-user scenarios)

### GUI vs Code Comparison:

| Aspect | GUI Approach | Code Approach |
|--------|--------------|---------------|
| Setup Time | 5-10 minutes | 30+ minutes |
| Coding Required | None | Python knowledge |
| Debugging | Use chat interface | Read code/logs |
| Customization | Limited to UI options | Unlimited |
| Deployment | Built-in | Manual setup |
| Best For | Quick demos, learning | Production apps |

## 🔧 Advanced Customization

### Adding More Scratchpad Sections

Edit your scratchpad file to include:

```markdown
## User Preferences

## Travel History
<!-- Past trips for reference -->

## Wishlists
<!-- Dream destinations -->

## Completed Tasks

## Future Bookings
<!-- Upcoming trips -->
```

### Using Multiple Scratchpad Files

For different contexts:
- `preferences_scratchpad.md` - User preferences only
- `tasks_scratchpad.md` - Task history
- `bookings_scratchpad.md` - Active bookings

Upload all files and instruct the agent which to use when.

### Automated Scratchpad Updates

For production scenarios, consider:
- **Power Automate**: Trigger scratchpad updates from external events
- **Logic Apps**: Sync scratchpad with databases
- **Azure Functions**: Custom scratchpad management logic

## 🚨 Common Issues & Solutions

### Issue: Agent doesn't update scratchpad

**Solution:**
- Make instructions MORE explicit: "You MUST update the scratchpad"
- Give examples of exact format to use
- Test with simple preferences first

### Issue: Agent forgets to check scratchpad

**Solution:**
- Add to instructions: "FIRST ACTION: Always read vacation_scratchpad.md"
- Remind agent in user message: "Please check my preferences first"

### Issue: Scratchpad becomes too large

**Solution:**
- Periodically download and archive old entries
- Upload a cleaned version
- Or use summarization before uploading

### Issue: Multiple users overwriting each other

**Solution:**
- Use separate scratchpad files per user
- Name files: `scratchpad_user1.md`, `scratchpad_user2.md`
- Or upgrade to code-based approach with database

## 🎯 Real-World Applications

This GUI approach works well for:

- **Proof of Concepts**: Demonstrate context engineering quickly
- **Internal Tools**: Team assistants with shared memory
- **Training**: Teach context concepts without coding
- **Rapid Prototyping**: Test ideas before coding
- **Simple Use Cases**: Single-user or small-team scenarios

## 📚 Next Steps

### Within Azure AI Foundry:
- Add **Code Interpreter** tool for calculations
- Enable **Function Calling** for external APIs
- Configure **Multiple agents** sharing scratchpad

### Transition to Code:
- Follow the [Python implementation](./code_samples/12-python-agent-framework.ipynb) for programmatic control
- Replace file storage with Cosmos DB
- Implement vector search over scratchpad entries

### Advanced Memory:
- Move to **Lesson 13** for database-backed memory
- Explore **semantic search** over historical preferences
- Build **knowledge graphs** from scratchpad data

## 🔗 Related Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [File Search Tool Guide](https://learn.microsoft.com/azure/ai-studio/how-to/agents-file-search)
- [Agent Builder Best Practices](https://learn.microsoft.com/azure/ai-studio/how-to/agents)
- [Lesson 7: Planning & Design](../07-planning-design/README.md) - Base Travel Agent
- [Lesson 13: Agent Memory](../13-agent-memory/README.md) - Advanced memory patterns

## 🤝 Integration with Lesson 7 & 13

This lesson builds a bridge between:

- **Lesson 7 (Planning/Design)**: You created the base Travel Agent
- **Lesson 12 (Context Engineering)**: You added scratchpad memory (this lesson!)
- **Lesson 13 (Agent Memory)**: You'll upgrade to database-backed, semantic memory

**Recommended Learning Path:**
1. Complete Lesson 7 → Build Travel Agent
2. Complete Lesson 12 (this guide) → Add context management
3. Complete Lesson 13 → Add advanced memory with vector search

---

**🎉 Congratulations!** You've implemented context engineering with persistent memory using only the Azure AI Foundry GUI!
