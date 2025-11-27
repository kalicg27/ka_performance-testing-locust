Performance Testing Framework (Locust)

This repository contains a performance testing framework built with Locust.
It is designed to load test REST APIs using configurable scenarios for read-heavy, write-heavy, and mixed behaviours.
The framework supports YAML-based configuration and automated CI execution via GitHub Actions.

1. Project Overview

The goal of this project is to provide a clean, extensible structure for performance testing.
It includes:

Multiple user behaviour classes

Centralised configuration

Headless and UI execution modes

CI integration for automated smoke performance tests

This project is part of a larger portfolio demonstrating skills in automation, performance testing, and backend test engineering.

2. Project Structure
performance-testing-locust/
├─ locustfile.py
├─ config/
│  └─ settings.yaml
├─ tests/
│  ├─ user_scenarios.py
│  └─ utils.py
├─ reports/                # local output, ignored in Git
├─ .github/
│  └─ workflows/
│     └─ locust-ci.yml
├─ requirements.txt
└─ README.md

3. Configuration

Test settings are defined in:
config/settings.yaml

Example:
target_host: "https://jsonplaceholder.typicode.com"

load_profile:
  users: 50
  spawn_rate: 5
  run_time: "1m"

endpoints:
  get_posts: "/posts"
  get_post: "/posts/1"
  get_users: "/users"
  create_post: "/posts"


This allows changing host, load profile, or endpoints without modifying test code.

4. User Scenarios
ReadOnlyUser

Simulates read-heavy workloads, performing GET requests such as:

/posts

/users

/posts/1

WriteHeavyUser

Simulates write-heavy traffic using POST requests, followed by read operations.

The framework is structured so additional user personas can easily be added.

5. Running the Tests
Install dependencies
pip install -r requirements.txt

Run in UI mode
locust -f locustfile.py


Open Locust web interface at:

http://localhost:8089/

Run in headless mode
locust -f locustfile.py --headless --users 50 --spawn-rate 5 --run-time 1m


Environment variable usage:

LOCUST_USERS=20 LOCUST_SPAWN_RATE=5 LOCUST_RUN_TIME=30s \
locust -f locustfile.py --headless

6. CI Integration

The project includes a GitHub Actions workflow:

.github/workflows/locust-ci.yml

CI performs a short headless performance test (smoke test) using:

configurable user load

configurable duration

only-summary output

This verifies framework stability on every push or pull request.

7. Reports

Locust can generate:

statistics tables

percentile response times

failure logs

Local report output can be stored inside the reports/ directory (excluded from version control).

8. Technologies Used

Python 3.11

Locust 2.x

PyYAML

GitHub Actions

JSONPlaceholder demo API

9. Purpose

This project demonstrates:

Ability to design structured performance testing frameworks

Understanding of load profiles, user simulation, and API behaviour

Experience with Locust and test automation tools

Integration of performance testing into CI pipelines

It forms the third component of a five-project automation engineering portfolio.