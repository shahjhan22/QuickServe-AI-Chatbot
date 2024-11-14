# Food Ordering and Tracking Chatbot - Dialogflow Project

A conversational chatbot for seamless food ordering and tracking using **Dialogflow**, **FastAPI**, and **MySQL**. This chatbot allows users to place, update, complete, and track food orders in real-time, delivering enhanced accuracy and customer engagement in food service.

---

## Problem Statement

The food ordering industry requires fast and reliable systems to manage customer orders accurately. Traditional methods often lead to delays, order inaccuracies, and high operational overhead. This project leverages Dialogflow’s natural language understanding (NLU) capabilities to create an intelligent chatbot for real-time food ordering and tracking, aimed at improving customer satisfaction and order handling efficiency.

---

## Table of Contents

- [Project Demo](#project-demo)
- [Key Features](#key-features)
- [Data Preprocessing](#data-preprocessing)
- [Data Engineering](#data-engineering)
- [Model Training](#model-training)
- [Working Flow](#working-flow)
- [Conclusion](#conclusion)

---

## Project Demo

The chatbot enables users to interact and manage their orders through natural language conversations:
1. **Order Items**: Users can add items to their order by specifying food items and quantities.
2. **Update Order**: Items can be removed or updated before finalizing the order.
3. **Complete Order**: Finalizes the order, provides the total amount, and confirms completion.
4. **Track Order**: Users can check the status of their order using a unique order ID.

### Example Interactions

- **Add Items**: "I'd like to add 2 pizzas and 1 mango lassi to my order."
- **Remove Items**: "Remove 1 pizza from my order."
- **Complete Order**: "Complete my order."
- **Track Order**: "What's the status of order ID 123?"

https://github.com/user-attachments/assets/17d60ea2-2bda-4a2d-aded-64df9e91a142


---

## Key Features

1. **Natural Language Processing**: Dialogflow interprets user intents and extracts entities for effective order handling.
2. **Order Tracking**: Real-time status updates are provided based on unique order IDs.
3. **Session Management**: Each user session retains order details until completion.
4. **Database Integration**: Uses MySQL for persistent storage of order details, tracking information, and history.

---

## Data Preprocessing

To enhance accuracy, the chatbot performs:
- **Entity Extraction**: Extracts specific food items and quantities from user inputs.
- **Parameter Mapping**: Maps Dialogflow parameters (e.g., food items, quantities) to database fields.
- **Error Handling**: Handles cases where items are unavailable, invalid quantities are specified, or users request unsupported items.

---

## Data Engineering

Data engineering for this project is focused on managing data flow between Dialogflow, FastAPI, and MySQL:
1. **Database Schema**:
   - **Orders Table**: Stores order information, including order ID, customer session, and total amount.
   - **Order Items Table**: Contains details of each item in an order, including food item name and quantity.
   - **Order Tracking Table**: Maintains the status of each order.

2. **Stored Procedures and Functions**:
   - `insert_order_item`: Adds items to an order.
   - `get_total_order_price`: Retrieves the total order cost upon completion.
3. **Session Storage**: Maintains active sessions in memory for ongoing orders to optimize response times.

---

## Model Training

This project utilizes Dialogflow’s NLU for intent and entity recognition, key to delivering accurate responses:
1. **Intent Detection**: Recognizes intents like "Add to Order," "Remove from Order," "Complete Order," and "Track Order."
2. **Entity Recognition**: Extracts specific entities such as food items and quantities from user input.
3. **Fulfillment Integration**: Uses FastAPI as a webhook to dynamically respond to user requests based on the recognized intent and entities.

### Models/Intents Used:
- **Order Management Intents**: Handles adding, removing, and updating items.
- **Order Completion Intent**: Triggers when the user wants to finalize the order.
- **Order Tracking Intent**: Responds to user requests to check the status of an order.
- **Order Add Intent** Etc

---

## Working Flow

1. **User Input**: The user interacts with the chatbot using natural language.
2. **Intent and Entity Recognition**: Dialogflow detects the intent and identifies entities (e.g., food items, quantities).
3. **Webhook Fulfillment**:
   - FastAPI receives the webhook request with the identified intent and entities.
   - Based on the intent, FastAPI interacts with MySQL to update the order details, calculate totals, or retrieve order status.
4. **Response Generation**: The chatbot generates a response to guide the user through the ordering process.

---

## Conclusion

This Dialogflow-powered food ordering and tracking chatbot streamlines order management in food service, enhancing operational accuracy and customer experience. By leveraging NLP for intent recognition and real-time fulfillment, this project demonstrates the potential for intelligent automation in food ordering and customer service scenarios.
