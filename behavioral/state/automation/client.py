from behavioral.state.automation.context.message import Message


def run():
    message = Message(subject="Issue #1050", body="Description Issue")
    message.send_to_operator()
    message.send_to_supervisor()
    message.send_to_internal_manager()
    message.send_to_managing_director()
    message.send_to_internal_manager()
    message.send_to_supervisor()
    message.send_to_operator()
    message.send_to_client()


if __name__ == '__main__':
    run()
