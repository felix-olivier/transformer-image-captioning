# Preprocess images: RGB, resize256, crop:224
# --> DONE

# Annotate article text
#   /scripts/annotate_ny_times
#   Each article get a list of NE & pos tags as: [{'start':, 'end':, 'text': , 'label(ne)/pos':}]
#   Maybe we do not need this for the model, because it seems pos tags are only used for statistics of the data set.
# --> SKIP

# Face detection
# --> SKIP

# ResNet image embeddings
# --> Done as part of main model

# Object detection
#   /scripts/annotate_yolov3
# --> DONE

# Byte-Pair article embeddings

