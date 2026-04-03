# 📦 DVC Data Versioning Project (Full Workflow Documentation)

---

## 🚀 Project Overview

This project demonstrates how to use **Git + DVC (Data Version Control)** to:

* Track datasets efficiently
* Store large data outside Git
* Version data like code
* Reproduce older versions anytime

---

## 🧠 Key Concepts

| Tool         | Purpose                     |
| ------------ | --------------------------- |
| Git          | Tracks code & metadata      |
| DVC          | Tracks data                 |
| Remote (s3/) | Stores actual dataset files |

---

## 📁 Project Structure

```
DVC_G1/
├── data/                 # Dataset (tracked by DVC)
├── s3/                   # Local remote storage
├── mycode.py             # Script to generate/update data
├── data.dvc              # DVC tracking file
├── .dvc/                 # DVC config
├── .gitignore
├── README.md
```

---

# 🔥 COMPLETE STEP-BY-STEP JOURNEY

---

## ✅ STEP 1: Clone Repository

```
git clone https://github.com/JiveshCodes/DVC_G1.git
cd DVC_G1
```

📌 Output: Repo cloned locally 

---

## ✅ STEP 2: Run Code to Generate Data

```
python mycode.py
```

✔ Created:

* `data/sample_data.csv`

---

## ✅ STEP 3: Initialize Git & Push Code

```
git init
git add .
git commit -m "1. Initialized git and updated code"
git push origin main
```

✔ Git now tracks:

* Code
* Data (initially)

---

## ❌ ERROR 1: DVC Not Installed

```
dvc init
```

❌ Error:

```
dvc : The term 'dvc' is not recognized
```

✔ Fix:

```
pip install dvc
```

📌 Also got warnings about PATH (safe to ignore for now)

---

## ✅ STEP 4: Initialize DVC

```
dvc init
git add .
git commit -m "2. Initialize DVC"
git push
```

✔ Created:

* `.dvc/`
* `.dvcignore`

---

## ✅ STEP 5: Create Remote Storage (Fake S3)

```
mkdir s3
dvc remote add -d myremote s3
git add .
git commit -m "3. Added DVC remote"
git push
```

✔ Now DVC knows where to store data

---

## ❌ ERROR 2: Data Already Tracked by Git

```
dvc add data/
```

❌ Error:

```
output 'data' is already tracked by SCM
```

✔ Fix:

```
git rm -r --cached data
git commit -m "4. Stop tracking data with Git"
```

📌 Explanation:

* Git ❌ should NOT track data
* DVC ✅ should track data

---

## ✅ STEP 6: Track Data with DVC

```
dvc add data/
git add .gitignore data.dvc
git commit -m "5. Track data with DVC"
git push
```

✔ Created:

* `data.dvc`
* `.gitignore` updated

---

## ✅ STEP 7: Push Data to Remote

```
dvc push
```

✔ Data stored inside:

```
s3/files/md5/
```

📌 These are hashed files (compressed + versioned)

---

## ✅ STEP 8: Version 1 (V1)

```
git commit -m "Version 1 of data"
git push
```

✔ First dataset version saved

---

## 🔄 STEP 9: Modify Data (V2)

Run:

```
python mycode.py
```

✔ Added new row

Check changes:

```
dvc status
```

---

## ✅ STEP 10: Save Version 2

```
dvc commit
dvc push
git commit -m "Version 2 of data"
git push
```

✔ Changes:

* Old data ❌ replaced
* New hashed files ✔ added

---

## 🔄 STEP 11: Modify Data Again (V3)

```
python mycode.py
dvc status
```

---

## ✅ STEP 12: Save Version 3

```
dvc commit
dvc push
git add .
git commit -m "Version 3 of data"
git push
```

✔ Now you have:

* V1
* V2
* V3

---

# ⏪ TIME TRAVEL (MOST IMPORTANT)

## ❌ ERROR 3: Wrong Command

```
git checkout <commit_id_of_V1>
```

❌ Error:

```
'<' operator is reserved
```

✔ Correct:

```
git checkout b9579b8
dvc checkout
```

✔ Result:

* Data reverted to **Version 1**

---

## 🔙 Return to Latest Version

```
git checkout main
dvc checkout
```

✔ Back to latest data (V3)

---

# 📊 WHAT CHANGED INTERNALLY

### Git tracks:

* `.dvc` files
* Code
* Metadata

### DVC tracks:

* Actual dataset
* Stored in `s3/files/md5`

---

# ⚠️ COMMON ERRORS (IMPORTANT)

### 1. DVC not recognized

✔ Fix:

```
pip install dvc
```

---

### 2. Data already tracked by Git

✔ Fix:

```
git rm -r --cached data
```

---

### 3. Forgot `dvc commit`

✔ Symptom:

```
dvc status shows modified
```

✔ Fix:

```
dvc commit
```

---

### 4. Used `<commit_id>`

✔ Fix:
Use actual commit hash:

```
git checkout b9579b8
```

---

# 🎯 FINAL OUTCOME

✔ Git + DVC fully integrated
✔ Data versioning working
✔ Remote storage configured
✔ 3 dataset versions created
✔ Time travel working

---

# 🏁 CONCLUSION

This project demonstrates a **real-world data versioning workflow** where:

* Code is versioned with Git
* Data is versioned with DVC
* Storage is separated from Git

---

# 💡 BONUS

You can extend this by:

* Using AWS S3 instead of local folder
* Adding ML models
* Creating pipelines with DVC

---
