import json
import os

def convert_to_iiif(input_path):
    """将OCR输出的JSON转换为IIIF注释格式"""
    
    # 读取输入文件
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 自动生成基础URL
    base_url = "https://oushiei120.github.io/iiif_test/docs"
    
    # 创建annotations列表
    annotations = []
    
    # 处理段落
    for i, para in enumerate(data.get('paragraphs', [])):
        if not para.get('contents'):
            continue
            
        box = para['box']
        annotation = {
            "id": f"{base_url}/annotation/p1-text-{i+1}",
            "type": "Annotation",
            "motivation": "commenting",
            "body": {
                "type": "TextualBody",
                "value": para['contents'],
                "language": "ja"
            },
            "target": {
                "source": f"{base_url}/canvas/p1",
                "selector": {
                    "type": "FragmentSelector",
                    "value": f"xywh={box[0]},{box[1]},{box[2]-box[0]},{box[3]-box[1]}"
                }
            }
        }
        annotations.append(annotation)
    
    # 创建IIIF AnnotationPage
    iiif_data = {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "id": f"{base_url}/annotation1.json",
        "type": "AnnotationPage",
        "items": annotations
    }
    
    # 生成输出文件路径
    output_dir = os.path.dirname(input_path)
    output_filename = os.path.splitext(os.path.basename(input_path))[0] + "_iiif.json"
    output_path = os.path.join(output_dir, output_filename)
    
    # 保存IIIF JSON文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(iiif_data, f, ensure_ascii=False, indent=2)
    
    print(f"转换完成！输出文件：{output_path}")
    return output_path

if __name__ == "__main__":
    # 设置输入文件路径
    input_path = "/Users/oushiei/Documents/GitHub/iiif_test/docs/resources/page1_page1_p1.json"
    
    # 执行转换
    output_path = convert_to_iiif(input_path)
