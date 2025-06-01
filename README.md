# 💧 Vext-Powered RAG Chatbot for Water Purifier Company

This is a **Retrieval-Augmented Generation (RAG)** chatbot built using [Vext](https://github.com/vext-ai/vext), designed for a water purifier company's customer support system.

It uses a custom pipeline of **two LLMs**, a **vector database**, and a **PDF-based knowledge base** to provide contextual, accurate responses to product-related questions.

---

## 🧠 Architecture (5-Stage Pipeline)

1. **Input Received**:  
   The chatbot receives a question from the user, called the `payload`.

2. **LLM 1 — GPT-4o Mini**:  
   Used to convert the user's question into keyword search terms.
   ```text
   System Prompt:
   Turn the question the user has asked below into a string of keywords that could be searched on Google to effectively find results about business-related questions.

   Question: 
   payload

   Only provide the keywords, nothing else:
