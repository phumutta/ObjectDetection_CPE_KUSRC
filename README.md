# ObjectDetection_CPE_KUSRC

ดาวน์โหลด Model ที่ใช้ในการตรวจจับ จำนวน 3 โมเดล ได้ที่ลิ้งด่านล่าง

Download https://drive.google.com/drive/folders/1zxfmNpSWc7GkgJwNcutAx_K1uXtAdlVY?usp=sharing        
*หมายเหตุ เมื่อทำการดาวน์โหลดแล้ว ให้นำไปไว้ที่ folder เดียวกับ folder detection

ในการใช้ ImageAI ในการพัฒนาแอพพลิเคชั่นของคุณคุณจะต้องทำการติดตั้งการพึ่งพาต่อไปนี้ก่อนที่จะทำการติดตั้ง ImageAI :

- Python 3.5.1 (และรุ่นที่ใหม่กว่า)
- pip3
- Tensorflow 1.4.0 (และเวอร์ชั่นที่ใหม่กว่า)
- Numpy 1.13.1 (และรุ่นที่ใหม่กว่า)
- SciPy 0.19.1 (และเวอร์ชั่นที่ใหม่กว่า)
- OpenCV
- Pillow
- h5py
- Keras 2.x

วิธีการใช้งานโปรแกรม

1. หลังจากที่ดาวน์โหลด model และ ติดตั้ง โมดูลข้างต้นหมดแล้ว ให้ทำการโหลดไฟล์ Design และ detection ไปไว้ในเครื่อง
2. ทำการเปิดโปรแกรม จาก folder detection ในไฟล์ที่มีชื่อว่า objectdetection3
3. เมื่อเปิดไฟล์แล้วให้ทำการ runcode แล้วจะขึ้นหน้าโปรแกรม
4. เลือก model และ ประเภท ที่ต้องการ detect แล้วกดปุ่ม Start
5. หากต้องการ Capture หน้าจอการ detect ให้กดที่ปุ่ม Capture แล้วโปรแกรมจะแสดงรูปทางด้านขวาของโปรแกรม
6. เมื่อต้องการหยุดการ detect ของโปรแกรม ให้กดปุ่ม Stop

ดังตัวอย่างด้านล่างนี้

![](https://camo.githubusercontent.com/f48d27ade3e89fcecd6d3baebb4a23f45d4f0c4c/68747470733a2f2f7777772e696d672e6c6976652f696d616765732f323031392f30342f32372f436170747572652e706e67)
