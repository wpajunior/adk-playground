from .dag import DAG, Node, NodeType

def get_order_status(order_id: str) -> str:
    """
    Retrieves the status of an order based on its ID.

    Args:
        order_id (str): The ID of the order to check.

    Returns:
        str: The status of the order that can be "Processing", "Shipped", "Delivered", or "Cancelled".

    """
    # statuses = {
    #     "123": "Processing",
    #     "456": "Shipped",
    #     "789": "Delivered",
    #     "000": "Cancelled"
    # }

    return "Processing"  # Simulated response for the sake of example

def cancel_order(order_id: str, reason: str) -> bool:
    """
    Cancels an order based on its ID and a reason.

    Args:
        order_id (str): The ID of the order to cancel.
        reason (str): The reason for cancelling the order.

    Returns:
        bool: True if cancellation was successful, False otherwise.

    """
    # Here you would typically interact with a database or service
    # For this example, we will simulate a successful cancellation

    return True  # Simulated response for the sake of example


def compensate_customer(customer_id: str, amount: float) -> bool:
    """
    Compensates a customer with a specified amount.

    Args:
        customer_id (str): The ID of the customer to compensate.
        amount (float): The amount to compensate the customer.

    Returns:
        bool: True if compensation was successful, False otherwise.

    """
    # Here you would typically interact with a payment system or database
    # For this example, we will simulate a successful compensation

    return True  # Simulated response for the sake of example


def is_vip_customer(customer_id: str) -> bool:
    """
    Checks if a customer is a VIP based on their ID.

    Args:
        customer_id (str): The ID of the customer to check.

    Returns:
        bool: True if the customer is a VIP, False otherwise.

    """
    # vip_customers = {"VIP123", "VIP456", "VIP789"}

    return True  # Simulated response for the sake of example


def close_case(case_id: str) -> bool:
    """
    Closes a customer service case based on its ID.

    Args:
        case_id (str): The ID of the case to close.

    Returns:
        bool: True if the case was successfully closed, False otherwise.

    """
    # Here you would typically interact with a case management system
    # For this example, we will simulate a successful case closure

    return True  # Simulated response for the sake of example


def sop_search(query: str) -> str:
    """
    Searches a standard operating procedure (SOP) for a specific query.

    Args:
        query (str): The query to search for in the SOP.

    Returns:
        str: A string representing the SOP id

    """
    # Here you would typically perform a search in a DAG structure
    # For this example, we will simulate a successful search

    return "dag_order_cancellation"  # Simulated response for the sake of example


def get_customer_id() -> str:
    """
    Retrieves the customer ID from the state.

    Returns:
        str: The customer ID.

    """
    # Here you would typically retrieve the customer ID from the state
    # For this example, we will simulate a customer ID

    return "customer_123"  # Simulated response for the sake of example


def get_sop_step(sop_id: str, step: int) -> str:
    """
    Retrieves a standard operating procedure (SOP) step

    Args:
        sop_id (str): The ID of the SOP to retrieve.
        step (int): The step number in the SOP to retrieve.

    Returns:
        str: A string representing the SOP content.

    """

    sop = DAG()
    node = Node(0, NodeType.DATA_EVALUATION)
    node.content = "Check if the order id is provided in state['order_id']. If not, go to step 1. If yes, continue to step 2."
    sop.add_node(node)

    node = Node(1, NodeType.USER_INPUT)
    node.content = "Ask the user for the order id and save it in state['order_id']. Iterate with the user until a valid order id is provided and then continue to step 2."
    sop.add_node(node)

    node = Node(2, NodeType.DATA_EVALUATION)
    node.content = "Check if the order is already cancelled. If yes, close the case and go to step 14. If no, continue to step 3."
    sop.add_node(node)

    node = Node(3, NodeType.DATA_EVALUATION)
    node.content = "Check if the user is a VIP customer. If yes, continue to step 4. If no, continue to step 10."
    sop.add_node(node)

    node = Node(4, NodeType.ACTION_EXECUTION)
    node.content = "Tell the customer that you are very sorry for the inconvenience and continue to step 5."
    sop.add_node(node)

    node = Node(5, NodeType.USER_INPUT)
    node.content = "Ask the customer for the reason of cancellation if the user hasn't mentioned it yet. Iterate until a valid reason is provided and continue to step 6."
    sop.add_node(node)

    node = Node(6, NodeType.ACTION_EXECUTION)
    node.content = "If reason for cancellation is 'delayed delivery', create a 2 euro compensation voucher. Tell the user about the voucher. Continue to step 7."
    sop.add_node(node)

    node = Node(7, NodeType.ACTION_EXECUTION)
    node.content = "Tell the customer that he/she will receive the refund automatically within 2-3 days and continue to step 8."
    sop.add_node(node)

    node = Node(8, NodeType.ACTION_EXECUTION)
    node.content = "Cancel the order and continue to step 9."
    sop.add_node(node)

    node = Node(9, NodeType.ACTION_EXECUTION)
    node.content = "Tell the customer that the order has been cancelled and that he/she will receive a confirmation email. Close the case. Go to step 14."
    sop.add_node(node)

    node = Node(10, NodeType.USER_INPUT)
    node.content = "Ask the customer for the reason of cancellation if the user hasn't mentioned it yet. Iterate until a valid reason is provided and continue to step 11."
    sop.add_node(node)

    node = Node(11, NodeType.ACTION_EXECUTION)
    node.content = "Tell the customer that he/she will receive the refund automatically within 2-3 days. Continue to step 12."
    sop.add_node(node)

    node = Node(12, NodeType.ACTION_EXECUTION)
    node.content = "Cancel the order and continue to step 13."
    sop.add_node(node)

    node = Node(13, NodeType.ACTION_EXECUTION)
    node.content = "Say goodbye and close the case. Continue to step 14."
    sop.add_node(node)

    node = Node(14, NodeType.ACTION_EXECUTION)
    node.content = "DONE"
    sop.add_node(node)

    print(f"Requested SOP step: {step}")

    return sop.nodes[step].get_content()  # Return the content of the requested SOP step