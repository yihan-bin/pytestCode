import  yaml
filename='E:\ChromeCoreDownloads\yolov5-master\models\yolov5l.yaml'
with open(filename, errors='ignore') as f:
    hyp = yaml.safe_load(f)  # load hyps dict
print(hyp)