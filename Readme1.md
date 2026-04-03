# 📦 DVC Data Versioning Project

## 🚀 Overview

This project demonstrates how to implement **data version control using DVC (Data Version Control)** integrated with **Git**.

It showcases how to:

* Track large datasets efficiently
* Version data alongside code
* Store data in remote storage
* Reproduce and revert to previous data versions

---

## 🧠 Key Concepts

| Tool         | Purpose                  |
| ------------ | ------------------------ |
| Git          | Tracks code and metadata |
| DVC          | Tracks large data files  |
| Remote (s3/) | Stores actual data       |

---

## 📁 Project Structure

```
DVC_G1/
│
├── data/                  # Dataset folder
│   └── sample_data.csv
│
├── s3/                    # Local remote storage (simulated S3)
│
├── mycode.py              # Script to generate/update dataset
├── data.dvc               # DVC pointer file
├── .dvc/                  # DVC internal files
├── .dvcignore             # Ignore rules for DVC
├── .gitignore             # Ignore rules for Git
├── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd DVC_G1
```

---

### 2️⃣ Install DVC

```bash
pip install dvc
```

---

### 3️⃣ Initialize DVC

```bash
dvc init
git add .
git commit -m "Initialize DVC"
```

---

### 4️⃣ Create Remote Storage

```bash
mkdir s3
dvc remote add -d myremote s3
git add .
git commit -m "Add DVC remote"
```

---

## 📊 Data Versioning Workflow

---

### 🔹 Step 1: Generate Initial Data (V1)

Run:

```bash
python mycode.py
```

Track with DVC:

```bash
dvc add data/
git add .gitignore data.dvc
git commit -m "Track data with DVC"
```

Push data:

```bash
dvc push
git commit --allow-empty -m "Version 1 of data"
git push
```

---

### 🔹 Step 2: Create Version 2 (V2)

Modify dataset (append new row via script):

```bash
python mycode.py
```

Check changes:

```bash
dvc status
```

Save new version:

```bash
dvc commit
dvc push
git add .
git commit -m "Version 2 of data"
git push
```

---

### 🔹 Step 3: Create Version 3 (V3)

Repeat same steps:

```bash
python mycode.py
dvc commit
dvc push
git add .
git commit -m "Version 3 of data"
git push
```

---

## 📦 Dataset Versions

| Version | Description              |
| ------- | ------------------------ |
| V1      | Initial dataset (3 rows) |
| V2      | Added "David"            |
| V3      | Added "Emma"             |

---

## 🔁 Time Travel (Reproducibility)

### 🔹 Go to Version 1

```bash
git checkout <commit_id>
dvc checkout
```

---

### 🔹 Go back to latest version

```bash
git checkout main
dvc checkout
```

---

## 🔥 Key Learnings

* Separation of **code and data**
* Efficient handling of large files
* Reproducibility of experiments
* Data version tracking similar to Git

---

## ⚠️ Important Notes

* `data/` is NOT tracked by Git directly
* `data.dvc` is a pointer file tracked by Git
* Actual data is stored in:

  ```
  .dvc/cache/ and s3/
  ```

---

## 🧩 How It Works

```
Git → tracks data.dvc
DVC → tracks actual data
Remote → stores data versions
```

---

## 🎯 Use Cases

* Machine Learning pipelines
* Data science experiments
* Large dataset management
* Collaborative data workflows

---

## 🚀 Future Improvements

* Integrate with AWS S3
* Add DVC pipelines
* Automate ML workflows
* Add experiment tracking

---

## 🏁 Conclusion

This project demonstrates a complete **end-to-end data versioning system** using DVC and Git.

You can:

* Track changes in datasets
* Store versions efficiently
* Reproduce any version anytime

---

## 👨‍💻 Author

**Your Name**

---

## ⭐ If you found this helpful, give it a star!
