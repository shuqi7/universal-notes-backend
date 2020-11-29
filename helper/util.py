def get_response(success, message, additional_arguments):
    """
    Return response for API to return
    """
    response = {
        'success': success,
        'message': message,
    }
    if additional_arguments:
        response.update(additional_arguments)

    return response