# ParseMessage-vk

* Very easy
* Fast
* Useful

 ## Usage:
 
 * Init it
 ```python
from ParsersMessage import ParseMessage, ParseReplyMessage
```
* Do parse:
```python
longpoll_message_object_json = {}
msg = ParseMessage(longpoll_message_object_json)
```
* Use:
```python
date = msg.date  #  Unix timestamp 
vk_id = msg.vk_id #  User id, who send message
msgid = msg.id  # Message id (Only for private messages)
out = msg.out  # ?-?
peer_id = msg.peer_id  # Chat id 
text = msg.text  #  Message text, Lower(!)
full_text = msg.full_text  #  Message text, not Lower(!)
conversation_message_id = msg.conversation_message_id  # Conversation message id
fwd_messages = msg.fwd_messages  # List of forward messages
important = msg.important  # ?-?
random_id = msg.random_id  # Random id
attachments = msg.attachments  # Msg attachments
is_hidden = msg.is_hidden  # Та я не знаю, АААААААААА
reply_message = msg.reply_message  # dict with one message

data = msg.data  # msg.data = longpoll_message_object_json
splitter = msg.splitter  # msg.splitter = msg.text.split(' ')
len = msg.len  # Len of msg.splitter
```

* Or parse forward messages:
```python
from ParsersMessage import ParseMessage, ParseReplyMessage

longpoll_message_object_json = {}
msg = ParseMessage(longpoll_message_object_json)
fwd = ParseReplyMessage(msg)
```
* And use second:
```python
if fwd.is_fwd_message is True:
    for i in fwd.text:
        print(fwd.text[i])
# And u may use this:
# fwd.data[i]
# fwd.date[i]
# fwd.vk_id[i]
# fwd.text[i]
# fwd.full_text[i]
# fwd.attachments[i]
# fwd.conversation_message_id[i]
# fwd.peer_id[i]
# fwd.id[i]
# fwd.update_time[i]
# fwd.len[i]
```

### Links!

- [Python](python.org)

- [Link to this project](https://github.com/SantaSpeen/ParseMessage-vk.Python)

- [Author](https://vk.com/id370926160)