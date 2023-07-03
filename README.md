# Mask Detection Using YOLOv5
## Problem Statement📝
COVID-19 pandemic has rapidly affected our day-to-day life disrupting the world trade and movements. Wearing a protective face mask has become a new normal. In the near future, many public service providers will ask the customers to wear masks correctly to avail of their services. Therefore, face mask detection has become a crucial task to help global society.
COVID-19 mask detector could potentially be used to help ensure your safety and the safety of others
## Dataset 📰
Dataset is collected using [Roboflow](https://public.roboflow.com/object-detection/mask-wearing)
```
mask_detection
  - train
    - images
    - labels
  - test
    - images
    - labels
  - valid
    - images
    - labels
  - data.yaml
```
## Model Performance
We had used YOLOv5 model and trained on 300 epochs with 82.9% of mAP50 score
![results](https://github.com/Parvez13/Mask_Detection/assets/66157611/7988ed8c-f97f-4b03-ae1d-1bd1fc9fef64)

![confusion_matrix](https://github.com/Parvez13/Mask_Detection/assets/66157611/a11fc963-f393-4dc0-be96-ad6897653c1b)
![val_batch1_pred](https://github.com/Parvez13/Mask_Detection/assets/66157611/fc19e187-9a55-4129-9cc5-8298bbc33bfb)
![val_batch0_pred](https://github.com/Parvez13/Mask_Detection/assets/66157611/c10f7f3e-b595-4bcb-a2c0-108155a050fa)


* AWS Cloud Deployment App Link on EC2 with Github Actions: https://54.241.138.215/8080
