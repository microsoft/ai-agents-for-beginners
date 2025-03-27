[![AI Agents In Production](./images/lesson-10-thumbnail.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Click the image above to view video of this lesson)_
# AI Agents in Production

## Introduction

This lesson will cover:

- How to plan the deployment of your AI Agent to production effectively.
- Common mistakes and issues that you may face when deploying your AI Agent to production.
- How to manage costs while still maintaining the performance of your AI Agent.

## Learning Goals

After completing this lesson, you will know how to/understand:

- Techniques for improving the performance, costs, and effectiveness of a production AI Agent system.
- What and how to evaluate your AI Agents.
- How to control costs when deploying AI Agents to production.

It is important to deploy AI Agents that are trustworthy. Check out the "Building Trustworthy AI Agents" lesson as well.

## Evaluating AI Agents

Before, during, and after deploying AI Agents, having a proper system to evaluate your AI Agents is critical. This will ensure that your system is aligned with you and your users' goals.

To evaluate an AI Agent, it is important to have the ability to evaluate not only the agent's output but also the entire system that your AI Agent is operating in. This includes but is not limited to:

- The initial model request.
- The agent's ability to identify the intent of the user.
- The agent's ability to identify the right tool to perform the task.
- The tool's response to the agent's request.
- The agent's ability to interpret the tool's response.
- The user's feedback to the agent's response.

This allows you to identify areas for improvement in a more modular way. You can then monitor the effect of changes to models, prompts, tools, and other components with better efficiency.

## Common Issues and Potential Solutions with AI Agents

| **Issue**                                      | **Potential Solution**                                                                                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI Agent not performing tasks consistently     | - Refine the prompt given to the AI Agent; be clear on objectives.<br>- Identify where dividing the tasks into subtasks and handling them by multiple agents can help.                                                      |
| AI Agent running into continuous loops         | - Ensure you have clear termination terms and conditions so the Agent knows when to stop the process.<br>- For complex tasks that require reasoning and planning, use a larger model that is specialized for reasoning tasks. |
| AI Agent tool calls are not performing well    | - Test and validate the tool's output outside of the agent system.<br>- Refine the defined parameters, prompts, and naming of tools.                                                                                        |
| Multi-Agent system not performing consistently | - Refine prompts given to each agent to ensure they are specific and distinct from one another.<br>- Build a hierarchical system using a "routing" or controller agent to determine which agent is the correct one.         |

## Managing Costs

Here are some strategies to manage the costs of deploying AI Agents to production:

- **Caching Responses** - Identifying common requests and tasks and providing the responses before they go through your agentic system is a good way to reduce the volume of similar requests. You can even implement a flow to identify how similar a request is to your cached requests using more basic AI models.

- **Using Smaller Models** - Small Language Models (SLMs) can perform well on certain agentic use-cases and will reduce costs significantly. As mentioned earlier, building an evaluation system to determine and compare performance vs larger models is the best way to understand how well an SLM will perform on your use case.

- **Using a Router Model** - A similar strategy is to use a diversity of models and sizes. You can use an LLM/SLM or serverless function to route requests based on complexity to the best fit models. This will also help reduce costs while also ensuring performance on the right tasks.

## Congratulations

This is currently the last lesson of "AI Agents for Beginners".

We plan to continue to add lessons based on feedback and changes in this ever growing industry so stop by again in the near future.

If you want to continue your learning and building with AI Agents, join the <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

We host workshops, community roundtables and "ask me anything" sessions there.

We also have a Learn collection of additional materials that can help you start building AI Agents in production.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)
