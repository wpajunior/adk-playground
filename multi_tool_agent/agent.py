from google.adk.agents import Agent
from .tools import *

knowledge_base_agent = Agent(
    name="knowledge_base_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that provides information from the knowledge base. "
        "It can answer questions, and provide documentation"
    ),
    instruction=(
        "You are a knowledge base agent. "
        "You will answer questions and provide documentation from the knowledge base. "
        "This is just a test, so you can use your imagination to answer questions. Just keep in mind that this is an customer service for a food delivery company."
    ),
)

sop_agent = Agent(
    name="sop_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that provides standard operating procedures (SOPs) for various tasks. "
        "It can execute predefined SOPs to fulfill customer requests."
    ),
    instruction=(
        "You are a SOP agent. You execute standard operating procedures (SOPs) for various tasks. "
        "You will receive a SOP id in state['sop_id'] and you must execute the SOP step by step, by calling the tool get_sop_step(sop_id, step) and executing the instructions provided until you get the instruction 'DONE'"
        "Start from step 0 as soon as the parent agent transfers the control to you. "
        "You shouldn´t tell the customer anything about the SOP or its steps, just execute the SOP steps and only communicate with the user if the step instructs you to do so"
    ),
        tools=[cancel_order, close_case, compensate_customer, get_customer_id, get_order_status, get_sop_step, is_vip_customer]
)

root_agent = Agent(
    name="coordinator_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that handles customer requests and delegates the handling to appropriate agents."
    ),
    instruction=(
        "You are a friendly coordinator agent that identifies the reason for customer requests and delegates them to the appropriate agents. "
        "If you can find a SOP that matches the request, you will save the SOP id in state['sop_id'] and delegate the request to the SOP agent. "
    ),
    sub_agents=[knowledge_base_agent, sop_agent],
    tools=[sop_search]
)
