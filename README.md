# 🧠 NanoGPT Deployment & Smoke Test

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)
![Status](https://img.shields.io/badge/Status-Operational-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Introduction

This repository is a lightweight deployment and verification implementation based on [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT).

The primary goal of this project is to demonstrate a **complete end-to-end LLM lifecycle**—from data generation to model training and inference—verified within a minimal compute environment (e.g., Google Colab T4 or local CPU/GPU).

We utilize a synthetic **"Tick Tock" pattern dataset** (or arithmetic logic) to conduct a "Smoke Test," ensuring that the model architecture, optimizer, and training loop are functioning correctly before scaling up to larger datasets like OpenWebText.

## 🚀 Features

- **Automated Data Pipeline**: Scripts to generate synthetic training data instantly.
- **Minimalist Configuration**: A tuned `smoke_test.py` config optimized for speed (trains in <30 seconds).
- **Deployment Ready**: Verified on Cloud (Colab) and Local environments.
- **Inference Verification**: Includes scripts to validate if the model has "learned" the pattern.

## 📂 Project Structure

```text
nanoGPT/
├── config/
│   ├── smoke_test.py      # <--- Custom config for rapid testing
│   └── train_shakespeare.py
├── data/
│   └── smoke_test/        # Generated binary data (excluded from git)
├── model.py               # GPT Model Definition
├── train.py               # Training Script
├── sample.py              # Inference/Sampling Script
├── test_deploy.py         # Unit tests for environment checks
└── README.md