# Zoo Recordings Service

## Overview
The **Zoo Recordings Service** is a FastAPI-based microservice that handles audio recordings related to the zoo. This includes:
- **Species Sounds**: General sounds made by species and scientist narrations.
- **Zoo Animal Sounds**: Recordings from specific animals at the zoo.
- **Environmental Sounds**: Background sounds from different zoo habitats.

The service uses **MongoDB** for flexible audio storage and retrieval, making it easier to manage structured and unstructured multimedia data.

---

## Features
- **FastAPI**: High-performance Python web framework.
- **MongoDB**: NoSQL database optimized for storing audio metadata.
- **Pydantic**: Data validation and serialization.
- **Poetry**: Dependency and environment management.
- **Docker-ready**: Easily deployable with containerization.

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/zoo-recordings-service.git
cd zoo-recordings-service
```

### 2. Install Dependencies
Make sure you have **Poetry** installed:
```sh
poetry install
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root:
```
MONGO_URI=your-monogdb-url
```

### 4. Run the Service
```sh
poetry run uvicorn app.main:app --reload
```

---

## Project Structure
```
zoo-recordings-service/
│── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── database.py              # MongoDB connection
│   ├── models/                  # MongoDB schema definitions
│   ├── schemas/                 # Pydantic models for request validation
│   ├── routes/
│   │   ├── species_sounds.py    # Endpoints for species sounds
│   │   ├── zoo_animal_sounds.py # Endpoints for individual zoo animals
│   │   ├── environment_sounds.py# Endpoints for environment recordings
│   ├── services/
│   │   ├── species_sounds.py    # Database operations for species
│   │   ├── zoo_animals.py        # Database operations for zoo animals
│   │   ├── environments.py       # Database operations for environments
│── .env                         # Environment variables
│── requirements.txt             # Dependencies
│── Dockerfile                   # Docker setup
│── README.md                    # Documentation
```

---

## API Endpoints
### **1. Species Sounds**
| Method | Endpoint | Description |
|--------|------------|-------------|
| **GET** | `/api/species/{species_name}/sounds` | Get sounds for a species |
| **POST** | `/api/species/{species_name}/sounds` | Add a new species sound |

### **2. Zoo Animal Sounds**
| Method | Endpoint | Description |
|--------|------------|-------------|
| **GET** | `/api/zoo-animals/{animal_id}/sounds` | Get sounds for a specific zoo animal |
| **POST** | `/api/zoo-animals/{animal_id}/sounds` | Add a new zoo animal sound |

### **3. Environment Sounds**
| Method | Endpoint | Description |
|--------|------------|-------------|
| **GET** | `/api/environments/{habitat}/sounds` | Get environment sounds |
| **POST** | `/api/environments/{habitat}/sounds` | Add a new environment sound |

---

## Testing
Run tests using **pytest**:
```sh
poetry run pytest
```

---

## Deployment (Docker)
### 1. Build the Docker Image
```sh
docker build -t zoo-recordings-service .
```

### 2. Run the Container
```sh
docker run -p 8000:8000 zoo-recordings-service
```

---

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Commit and push changes.
4. Submit a pull request.

---

## License
MIT License. See `LICENSE` for details.

---

## Contact
Author: **Derek Gygax**  
Email: [derekgygax@gmail.com](mailto:derekgygax@gmail.com)

