# checkstyle: noqa
from twml.feature_config import FeatureConfigBuilder


def get_feature_config(data_spec_path, label):
  return FeatureConfigBuilder(data_spec_path=data_spec_path, debug=True) \
    .batch_add_features(
    [
        ("RANDOM BULLSHIT GO!!!!"),
    ]
  ).add_labels([
    label,                                   # Tensor index: 0
    "recap.engagement.is_clicked",           # Tensor index: 1
    "recap.engagement.is_favorited",         # Tensor index: 2
    "recap.engagement.is_open_linked",       # Tensor index: 3
    "recap.engagement.is_photo_expanded",    # Tensor index: 4
    "recap.engagement.is_profile_clicked",   # Tensor index: 5
    "recap.engagement.is_replied",           # Tensor index: 6
    "recap.engagement.is_retweeted",         # Tensor index: 7
    "recap.engagement.is_video_playback_50",  # Tensor index: 8
    "timelines.earlybird_score",             # Tensor index: 9
  ]) \
    .define_weight("meta.record_weight/type=earlybird") \
    .build()
