## Implementing messaging communication in Mesa

With the Mesa library, it is possible to set up indirect interaction mechanisms through the environment (like a blackboard). However, it does not handle direct interactions such as message communication. So, first, we will implement our own communication layer in Mesa. 

As seen previously, the messaging communication in MAS is a four step mechanism.

Before implementing the communicating agents and according to the picture, we must create: (1) a `Message` object, (2) a `Mailbox` object and (3) a list of allowed performative for messages. To do so, we create a new folder hierarchy containging: 

1- mesa: root folder which will contain your python codes using the communication layer;
2- communication: the root folder of the communication layer;
3- agent: the folder which will contain the implementation of the communicating agent class;

4- mailbox: the folder which will contain the implementation of the mailbox class. To manage messages, each communicating agent will have his own mailbox. The purpose of this class is to provide to agents some mechanisms for handling sent and received messages. The Mailbox class is composed of two attributes and five methods.

The two attributes of the Mailbox class are:

- unread_messages: the list of unread messages;
- read_messages: the list of read messages.

The five methods of the Mailbox class are:

- receive_messages(message): receive a message and add it in the unread messages list;
- get_new_messages(): return all the messages from unread messages list;
- get_messages(): return all the messages from both unread and read messages list;
- get_messages_from_performative(performative): return a list of messages which have the same performative;
- get_messages_from_exp(exp): return a list of messages which have the same sender.

5- message: the folder which will contain the implementation of the message and performative class. he purpose of this Message class is to create a python message object containing the receiver and sender identifiers but also the performative of the message sent as well as a content. Agents will exchange information using these items during their communication phases. The Message class is therefore composed of four attributes, four accessor methods (used to access the state of the object i.e, the data hidden in the object can be accessed from this method) and a string method (which returns a string, which is considered an informal or nicely printable representation of the message object).

The four attributes of the Message class are:

- from_agent: the sender of the message identified by its id;
- to_agent: the receiver of the message identified by its id;
- message_performative: the performative of the message;
- content: the content of the message.

The four accessor methods of the Message class are:

- get_exp(): return the sender of the message;
- get_dest(): return the receiver of the message;
- get_performative(): return the performative of the message;
- get_content(): return the content of the message.
