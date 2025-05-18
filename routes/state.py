from flask import Blueprint, request, jsonify
from utils.prompt_loader import load_prompt

state_bp = Blueprint('state', __name__)

# Dummy logic to simulate state transitions
def get_next_state(current_state):
    transitions = {
        "collect_city": "collect_contact_information",
        "collect_contact_information": "master_collect",
        "master_collect": "master_inform",
        "master_inform": "end"
    }
    return transitions.get(current_state, "end")

@state_bp.route("/api/next-state", methods=["POST"])
def next_state():
    data = request.json
    state = data.get("state")
    context = data.get("context", {})

    if not state:
        return jsonify({"status": "error", "message": "State is required"}), 400

    # Add dynamic context for specific states
    if state == "collect_contact_information":
        context.update({
            "validate_phone_number_tool_name": "PhoneValidatorTool",
            "prohibited_tools": "manualLookup",
            "name": context.get("name", ""),
            "phone_number": context.get("phone_number", "")
        })

    elif state == "master_inform":
        context.update({
            "what_to_inform": "booking confirmation",
            "tool_to_inform": "BookingTool",
            "next_step": "ask for review",
            "prohibited_words_list": "cheap, discount",
            "additional_context": ["Speak clearly", "Be polite"],
            "example_for_inform": "Your booking is confirmed! Thank you."
        })

    elif state == "master_collect":
        context.update({
            "entity_name": "email address"
        })

    prompt = load_prompt(state, context)
    next_state_val = get_next_state(state)

    return jsonify({
        "status": "success",
        "current_state": state,
        "prompt": prompt,
        "next_state": next_state_val
    })