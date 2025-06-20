import sys
def main():
    """
    ฟังก์ชันหลักของโปรแกรมสำหรับแสดงพารามิเตอร์ตัวแรก
    """
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")
if __name__ == "__main__":
    main()
