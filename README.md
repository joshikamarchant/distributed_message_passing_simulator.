# Distributed Message Passing Simulator

**Course:** CS3551 – Distributed Computing  
**Project type:** Python mini project  
**Student:** M. Joshika  
**Register Number:** 814724104062

## 1. Project Overview

The Distributed Message Passing Simulator is a beginner-friendly, menu-driven Python application that demonstrates how logical processes communicate by exchanging messages. It models four processes (`P1`, `P2`, `P3`, and `P4`) on a single computer.

This is an educational simulation. It does not create real network connections or run processes on separate computers.

## 2. Objectives

- Demonstrate message passing between logical processes.
- Implement unicast and broadcast communication.
- Demonstrate First-In, First-Out (FIFO) message queues.
- Maintain a communication event log.
- Display a simple summary of delivered and pending messages.

## 3. Features

- **Unicast:** Send a message from one process to another.
- **Broadcast:** Send a message to all processes except the sender.
- **FIFO receive:** Receive the oldest pending message first.
- **Message queues:** View pending messages for each process.
- **Event log:** View send/delivery and receive events.
- **Communication analysis:** View the number of message copies delivered and messages still pending.
- **Sample demonstration:** Run a ready-made example.

## 4. Technologies Used

- Programming language: Python
- Python concepts: Classes, functions, dataclasses, dictionaries, lists and FIFO queues (`collections.deque`)
- External packages: None

## 5. Requirements

- Python 3.8 or newer
- A terminal or command prompt

## 6. Project Files

```text
distributed-message-passing-simulator/
├── main.py
├── README.md
└── .gitignore
```

## 7. How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 main.py
   ```

## 8. Menu Options

| Option | Operation |
|---|---|
| 1 | Send a unicast message |
| 2 | Broadcast a message |
| 3 | Receive the next message |
| 4 | View message queues |
| 5 | View the event log |
| 6 | View communication analysis |
| 7 | Run the sample demonstration |
| 0 | Exit |

## 9. Sample Demonstration

Choose option `7` to run the built-in example:

- `P1` sends a request to `P2`.
- `P2` sends a reply to `P1`.
- `P3` broadcasts a message to `P1`, `P2`, and `P4`.

Then choose options `4`, `5`, and `6` to inspect the queues, event log, and communication analysis. Choose option `3` to receive queued messages one at a time.

## 10. Expected Learning Outcome

This project helps demonstrate logical processes, message passing, unicast, broadcast, FIFO queue behavior, and event logging in a distributed-computing context.

## 11. Limitations

- The four processes are logical representations within one Python program.
- Messages are stored in memory and are not sent over a real network.
- Message data is cleared when the program exits.

## 12. Conclusion

The Distributed Message Passing Simulator provides a simple way to understand basic communication operations used in distributed computing. It demonstrates how messages can be sent, queued, received, and recorded.

---

**Prepared by:** M. Joshika  
**Register Number:** 814724104062
