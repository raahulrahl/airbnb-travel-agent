<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center"> airbnb-travel-agent 🌻</h1>

<br/>

[![Build status](https://img.shields.io/github/actions/workflow/status/raahulrahl/airbnb-travel-agent/main.yml?branch=main)](https://github.com/raahulrahl/airbnb-travel-agent/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/raahulrahl/airbnb-travel-agent/branch/main/graph/badge.svg)](https://codecov.io/gh/raahulrahl/airbnb-travel-agent)
[![Commit activity](https://img.shields.io/github/commit-activity/m/raahulrahl/airbnb-travel-agent)](https://img.shields.io/github/commit-activity/m/raahulrahl/airbnb-travel-agent)
[![License](https://img.shields.io/github/license/raahulrahl/airbnb-travel-agent)](https://img.shields.io/github/license/raahulrahl/airbnb-travel-agent)

<br/>

An intelligent AI-powered travel assistant that helps users discover and plan their perfect accommodations using real-time Airbnb listings and Google Maps location data.

- **Github repository**: <https://github.com/raahulrahl/airbnb-travel-agent/>
- **Documentation**: <https://raahulrahl.github.io/airbnb-travel-agent/>

<br/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:raahulrahl/airbnb-travel-agent.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Configure API Keys

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
- **OPENROUTER_API_KEY**: Get from [OpenRouter](https://openrouter.ai/keys)
- **MEM0_API_KEY**: Get from [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys)

### 4. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 5. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

### 6. Configure Docker Hub Secrets (Optional)

To enable automatic Docker image builds and pushes to Docker Hub, add the following secret to your GitHub repository:

1. Go to your repository settings → Secrets and variables → Actions
2. Add a new repository secret:
   - **Name**: `DOCKERHUB_TOKEN`
   - **Value**: Your Docker Hub access token (create one at [Docker Hub Security Settings](https://hub.docker.com/settings/security))

The workflow will automatically build and push Docker images when changes are pushed to the `main` branch.


<br/>

# From Zero to Production-Ready Agent in 2 Minutes

**[Create Bindu Agent](https://github.com/getbindu/create-bindu-agent/tree/main)** is the fastest way to build production-ready AI agents that speak the language of the Internet of Agents. No boilerplate. No configuration hell. Just configure and get a fully deployable agent that communicates using **A2A**, **AP2**, and **X402** protocols.

<br/>

## Quickstart

**Time to first agent: ~2 minutes** ⏱️

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

<br/>

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong><br/>
  <em>Happy Bindu! 🌻🚀✨</em>
</p>

<p align="center">
  <strong>From idea to Internet of Agents in 2 minutes.</strong><br/>
  <em>Your agent. Your framework. Universal protocols.</em>
</p>

<p align="center">
  <a href="https://github.com/getbindu/create-bindu-agent">⭐ Star us on GitHub</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://docs.getbindu.com">📚 Read the Docs</a>
</p>
