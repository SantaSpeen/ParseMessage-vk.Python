class ParseMessage:
    def __init__(self, data: dict) -> None:
        """
        Парсинг сообщения
        :param data: -> json поля "message" от пула
        """
        self.date = data["date"]
        self.vk_id = data["from_id"]
        self.id = data["id"]
        self.out = data["out"]
        self.peer_id = data["peer_id"]
        self.text = data["text"].lower()
        self.full_text = data["text"]
        self.conversation_message_id = data["conversation_message_id"]
        self.fwd_messages = data["fwd_messages"]
        self.important = data["important"]
        self.random_id = data["random_id"]
        self.attachments = data["attachments"]
        self.is_hidden = data["is_hidden"]
        self.reply_message = data.get("reply_message")

        # "утилиты"
        self.data = data
        self.splitter = self.text.split(' ')
        self.len = len(self.splitter)


class ParseReplyMessage:

    def __init__(self, msg: ParseMessage) -> None:
        """
            Парсинг пересланных сообщений
            :param msg: -> self класса ParseMessage
            """
        self.reply_message = msg.reply_message
        self.fwd_messages = msg.data.get("fwd_messages")

        # Заглушки
        self.is_fwd_message = False
        self.date = None
        self.vk_id = None
        self.text = None
        self.full_text = None
        self.attachments = None
        self.conversation_message_id = None
        self.peer_id = None
        self.id = None
        self.update_time = None
        self.data = []
        self.len = 0

        if self.reply_message is not None:
            self.is_fwd_message = True
            self.data = [self.reply_message]
            self.date = [self.reply_message["date"]]
            self.vk_id = [self.reply_message["from_id"]]
            self.text = [self.reply_message["text"].lower()]
            self.full_text = [self.reply_message["text"]]
            self.attachments = [self.reply_message["attachments"]]
            self.conversation_message_id = [self.reply_message["conversation_message_id"]]
            self.peer_id = [self.reply_message.get("peer_id")]
            self.id = [self.reply_message.get("id")]
            self.update_time = [self.reply_message.get("update_time")]
            self.len = 1

        if self.fwd_messages:
            self.is_fwd_message = True
            self.data = self.fwd_messages
            self.date = [self.fwd_messages[i]["date"] for i in range(len(self.fwd_messages))]
            self.vk_id = [self.fwd_messages[i]["from_id"] for i in range(len(self.fwd_messages))]
            self.text = [self.fwd_messages[i]["text"].lower() for i in range(len(self.fwd_messages))]
            self.full_text = [self.fwd_messages[i]["text"] for i in range(len(self.fwd_messages))]
            self.attachments = [self.fwd_messages[i]["attachments"] for i in range(len(self.fwd_messages))]
            self.conversation_message_id = [
                self.fwd_messages[i]["conversation_message_id"] for i in range(len(self.fwd_messages))]

            self.peer_id = [self.fwd_messages[i].get("peer_id") for i in range(len(self.fwd_messages))]
            self.id = [self.fwd_messages[i].get("id") for i in range(len(self.fwd_messages))]
            self.update_time = [self.fwd_messages[i].get("update_time") for i in range(len(self.fwd_messages))]
            self.len = len(self.fwd_messages)
