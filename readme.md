# Docker Compose Documentation for Event Board Project

This document provides an overview of the `docker-compose.yml` configuration for the Event Board project, which consists of three services: `web`, `api`, and `db`.

## Services

### 1. Web (`web`)

This service is responsible for running the frontend of the Event Board project.

- **Build Context**: The Docker image for this service is built using the Dockerfile located in the `./event-board-web` directory.
  
- **Ports**: The service is exposed on port `3000` of the host machine, which is mapped to port `3000` inside the container.

- **Volumes**:
  - The local `./event-board-web` directory is mounted to `/usr/src/app` inside the container. This allows for real-time code changes without rebuilding the container.
  - A named volume for `node_modules` ensures that the dependencies remain persistent and are not overwritten by the host volume mount.

### 2. API (`api`)

This service is responsible for running the backend API of the Event Board project.

- **Build Context**: The Docker image for this service is built using the Dockerfile located in the `./event-board-api` directory.

- **Command**: On startup, this service runs a series of commands to:
  - Make database migrations.
  - Apply those migrations.
  - Start the Django development server on port `8000`.

- **Ports**: The service is exposed on port `8000` of the host machine, which is mapped to port `8000` inside the container.

- **Volumes**: The local `./event-board-api` directory is mounted to `/code` inside the container.

- **Environment Variables**:
  - Database configurations such as database name, user, password, host, and port.
  - An email host user for sending emails.
  - A development mode flag.

- **Dependencies**: This service depends on the `db` service, ensuring that the database is up and running before the API service starts.

### 3. Database (`db`)

This service is responsible for running a PostgreSQL database for the project.

- **Image**: Uses the official `postgres` image from Docker Hub.

- **Ports**: The service is exposed on port `5432` of the host machine, which is mapped to port `5432` inside the container.

- **Volumes**: The local `./event-board-api/data/db` directory is mounted to `/var/lib/postgresql/data` inside the container, ensuring data persistence across container restarts.

- **Environment Variables**: Configurations for the PostgreSQL database, such as database name, user, and password.

## Usage

To start all services:

```bash
docker-compose build
docker-compose up
```

To stop all services:

```bash
docker-compose down
```

## Conclusion

This `docker-compose.yml` configuration provides a seamless development environment for the Event Board project, ensuring that the frontend, backend, and database services work in harmony.
