
import os
import tensorflow as tf

annotation_folder = "/dataset/"
if not os.path.exists(os.path.abspath(".") + annotation_folder):
    print("donwloading")
    annotation_zip = tf.keras.utils.get_file(
        "val.tar.gz",
        cache_subdir=os.path.abspath("."),
        origin="http://diode-dataset.s3.amazonaws.com/val.tar.gz",
        extract=True,
    )