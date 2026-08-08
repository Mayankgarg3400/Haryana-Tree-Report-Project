🌱 VanMitra AI

Haryana Tree Plantation & Forest Intelligence Assistant

VanMitra AI is an Agentic RAG-based AI assistant designed to provide information and insights related to Haryana's forests, tree plantation, climate, soil, tree species, departmental contacts, and other forestry-related data.

The system combines Retrieval-Augmented Generation (RAG), multiple agents, ChromaDB, Ollama/Qwen, and MCP tools to retrieve relevant information from the project's knowledge base and generate grounded responses.

✨ Key Features

🤖 Agentic RAG for question answering over Haryana forestry data

🔎 Semantic retrieval using vector embeddings

🧠 Multiple agents for retrieval, analysis, recommendations, and RAG

🗃️ ChromaDB as the local vector database

🦙 Ollama + Qwen for local LLM inference

🌳 Haryana-specific tree plantation and forest information

🌦️ Weather-related MCP integration

🗺️ Map / Haryana GeoJSON integration

📄 Support for structured and unstructured project data

🔌 MCP servers/tools for extending the agent's capabilities

💬 Interactive application interface through app.py

🧠 Agentic RAG Architecture

                         ┌──────────────────────┐
                         │      User Query      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Agentic Layer     │
                         │  LangGraph / Agents  │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          Retrieval Agent     Analysis Agent   Recommendation Agent
                  │                 │                 │
                  └─────────────────┼─────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   RAG / Retriever    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      ChromaDB        │
                         │    Vector Store      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Relevant Context   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Ollama + Qwen LLM  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Grounded Answer    │
                         └──────────────────────┘

🛠️ Tech Stack

Technology

Purpose

Python

Core development

LangChain / LangGraph

RAG and agent orchestration

Ollama

Local model serving

Qwen

LLM

ChromaDB

Vector database

Embeddings

Semantic document retrieval

MCP

Tool/server integration

GeoJSON

Haryana map data

Pandas

Structured data processing

uv

Python dependency/environment management

📂 Project Structure

agentic-tree-rag/
│
├── agents/
│   ├── analysis_agent.py
│   ├── rag_agent.py
│   ├── recommendation_agent.py
│   └── retrieval_agent.py
│
├── data/
│   └── raw/
│       ├── docs/
│       ├── excel/
│       ├── maps/
│       └── reports/          # Large reports kept outside Git
│
├── mcp/
│   ├── csv_server.py
│   ├── filesystem_server.py
│   ├── map_server.py
│   └── weather_server.py
│
├── memory/
│   └── conversation.py
│
├── rag/
│   ├── embeddings.py
│   ├── loader.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vector_store.py
│
├── tools/
│   ├── csv_tool.py
│   └── map_tool.py
│
├── app.py
├── config.py
├── graph.py
├── ingest.py
├── main.py
├── prompts.py
├── test.py
├── pyproject.toml
├── requirement.txt
└── uv.lock

📊 Data

The project uses Haryana-focused datasets and documents covering areas such as:

Haryana forest and plantation information

Tree species

Climate information

Soil information

Departmental/contact information

District-level forestry information

Haryana map / GeoJSON data

Structured Excel data

Large Reports

Large source reports are intentionally not stored in GitHub because of their size.

The repository ignores:

data/raw/reports/
chroma_db/
.venv/
.env

The original reports can be placed locally in:

data/raw/reports/

before running the ingestion pipeline.

⚙️ Local Setup

1. Clone the repository

git clone https://github.com/Mayankgarg3400/VanMitra-AI-.git
cd VanMitra-AI-

2. Create / activate the virtual environment

Using uv:

uv sync

Or create a standard virtual environment:

python -m venv .venv
source .venv/bin/activate

On Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Install dependencies

If using uv:

uv sync

Or:

pip install -r requirement.txt

🦙 Ollama Setup

VanMitra AI currently uses local Ollama models.

Install Ollama and make sure the Ollama service is running.

Then pull the required models used by your local configuration.

Example:

ollama list

The project currently uses Qwen for local LLM inference and an Ollama embedding model for vector retrieval.

Model names should match the configuration in config.py / RAG modules.

🗃️ Build the Vector Database

After placing the required source documents inside:

data/raw/

run:

python ingest.py

This processes the documents, creates chunks, generates embeddings, and stores them in the local ChromaDB directory.

The generated vector database is:

chroma_db/

It is intentionally excluded from GitHub and should be generated locally.

🚀 Run the Application

Main CLI

python main.py

Application

python app.py

Use the entry point supported by your current application configuration.

💬 Example Questions

You can ask VanMitra AI questions such as:

Tell me about Neem trees in Haryana.

What is the tree plantation information for Kaithal?

Give information about Haryana's climate.

What soil information is available for Haryana?

Give the contact information of the Forest Department.

The assistant is designed to retrieve relevant information from the available project knowledge base instead of relying only on general model knowledge.

🔌 MCP Integration

The project contains MCP-related servers for extending the agentic system:

mcp/
├── csv_server.py
├── filesystem_server.py
├── map_server.py
└── weather_server.py

These components are intended to provide the agent with access to external/local tools such as:

CSV / structured data

File-system operations

Haryana map data

Weather information

🗺️ Map Data

The repository contains:

data/raw/maps/Haryana.geojson

This provides Haryana geographic/map information used by the map-related functionality.

🔐 Environment Variables

Keep secrets outside GitHub.

Create a local .env file if required by your configuration:

# Example
API_KEY=your_key_here

Never commit:

.env

to GitHub.

🛡️ Data & Security Notes

API keys and secrets should never be committed.

Large reports are excluded from Git.

ChromaDB is generated locally.

The virtual environment is excluded from Git.

Always verify .gitignore before pushing changes.

🚧 Future Improvements

Planned improvements can include:

🌐 Cloud deployment

📍 Interactive Haryana plantation map

📊 District-wise analytics dashboard

🌳 Tree plantation recommendations

🔄 Automated data updates

☁️ Cloud-hosted vector database

🤖 Production-grade hosted LLM

🔐 Authentication and user management

📈 Monitoring and evaluation of RAG responses

👨‍💻 Author

Mayank Garg

BTech — Information Technology

GitHub: @Mayankgarg3400

🌱 Project Goal

VanMitra AI aims to make Haryana forestry and tree plantation information easier to access through an intelligent, retrieval-grounded, agentic AI system.

Plant trees. Preserve forests. Build smarter environmental intelligence. 🌳🤖
