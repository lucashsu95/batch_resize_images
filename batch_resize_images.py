from PIL import Image
import os

def resize_images(input_folder, output_folder, width=1920):
    # 確保輸出資料夾存在
    os.makedirs(output_folder, exist_ok=True)

    # 取得輸入資料夾中的所有檔案
    files = os.listdir(input_folder)

    for file_name in files:
        # 檔案路徑
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # 開啟圖片
            img = Image.open(input_path)

            # 計算等比例高度
            aspect_ratio = img.width / img.height
            height = int(width / aspect_ratio)

            # 調整解析度
            resized_img = img.resize((width, height))

            # 儲存調整後的圖片
            resized_img.save(output_path)
            print(f"圖片 {file_name} 已調整為 {width} x {height}")
        except Exception as e:
            print(f"處理 {file_name} 時發生錯誤：{e}")

if __name__ == "__main__":
    input_folder = "C:/Users/user/Desktop/test/"
    output_folder = "C:/Users/user/Desktop/test/img"
    resize_images(input_folder, output_folder)
