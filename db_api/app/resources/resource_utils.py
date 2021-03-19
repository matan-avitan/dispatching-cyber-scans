def error_handler(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return {"result": "Failed", "error": str(e)}

    return handler
