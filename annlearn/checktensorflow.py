import tensorflow as tf
print("gpus ", len(tf.config.experimental.list_physical_devices('GPU')))
print("gpus logical ", len(tf.config.experimental.list_logical_devices('GPU')))


