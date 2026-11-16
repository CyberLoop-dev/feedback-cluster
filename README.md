<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=Feedback%20Cluster&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="Feedback Cluster banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Group%20similar%20feedback%20with%20lightweight%20TF-IDF" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/feedback-cluster/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/feedback-cluster?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/feedback-cluster/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/feedback-cluster?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/feedback-cluster?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="Feedback Cluster illustration"></p>

## 🧭 Overview
Cluster short feedback notes by word similarity using a small, explainable TF-IDF and cosine-similarity pipeline.

## ✨ Features
- 🧠 Build TF-IDF vectors without a hosted AI service.
- 🧩 Group similar notes using a configurable similarity threshold.
- 📄 Read one feedback item per line and export JSON clusters.
- 🔍 Keep the clustering logic small and inspectable.

## 🖥️ Demo
~~~bash
python main.py examples/feedback.txt --threshold 0.24 --output clusters.json
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/feedback-cluster.git
cd feedback-cluster
python main.py examples/feedback.txt --threshold 0.24 --output clusters.json
~~~

## 🧰 Tech Stack
- Python 3.10+
- re, math, json, argparse (standard library)

## 🗂️ Folder Structure
~~~text
feedback-cluster/\n├── assets/icon.svg\n├── examples/feedback.txt\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add CSV input with a configurable text column.
- [ ] Add cluster labels based on the most distinctive terms.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
