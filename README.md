# 📱 Android Use

**The open-source library for controlling native Android apps. Heavily inspired by [Browser Use](https://github.com/browser-use/browser-use).**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/Status-Public_Beta-orange)]()

**Android Use** connects your AI Agents to native Android applications. It creates a self-healing, semantic bridge between your LLM and the chaotic Android UI.

### ⚡ Why Android Use?

Building agents for mobile is hard. Vision APIs are slow, expensive, and flaky. `uiautomator` is brittle.

**Android Use** solves this by converting the raw Accessibility Tree into a lightweight, clean JSON representation.

* **💸 95% Cheaper:** Stops burning tokens on high-res screenshots. Uses text-only context.
* **🏎️ 10x Faster:** Zero image processing latency. Real-time execution.
* **🧠 Self-Healing:** Finds buttons by *meaning* ("Connect"), not just coordinates. If the UI changes, your agent adapts.

---

### 🚀 Quick Start

#### Prerequisites
1.  **Python 3.10+**
2.  **ADB Installed** (`brew install android-platform-tools`)
3.  **An Android Device** (Physical Pixel, Samsung, or Emulator) connected via USB/WiFi.

#### Installation

```bash
# Clone the repository
git clone [https://github.com/your-username/android-use.git](https://github.com/your-username/android-use.git)
cd android-use

# Install dependencies
pip install -r requirements.txt