from enum import IntEnum


class Code(IntEnum):
    INFO_UPLOADING = 2001
    INFO_WAITING = 2002
    INFO_LOADING = 2003
    INFO_MATCHING_LEVELS = 2004
    INFO_MATCHING_FREQS = 2005
    INFO_CORRECTING_LEVELS = 2006
    INFO_FINALIZING = 2007
    INFO_EXPORTING = 2008
    INFO_MAKING_PREVIEWS = 2009
    INFO_COMPLETED = 2010

    INFO_TARGET_IS_MONO = 2101
    INFO_REFERENCE_IS_MONO = 2201
    INFO_REFERENCE_IS_CLIPPING = 2202

    WARNING_TARGET_IS_CLIPPING = 3001
    WARNING_TARGET_LIMITER_IS_APPLIED = 3002
    WARNING_TARGET_IS_RESAMPLED = 3003

    ERROR_TARGET_LOADING = 4001
    ERROR_TARGET_LENGTH_IS_EXCEEDED = 4002
    ERROR_TARGET_LENGTH_IS_TOO_SMALL = 4003
    ERROR_TARGET_NUM_OF_CHANNELS_IS_EXCEEDED = 4004
    ERROR_TARGET_EQUALS_REFERENCE = 4005

    ERROR_REFERENCE_LOADING = 4101
    ERROR_REFERENCE_LENGTH_LENGTH_IS_EXCEEDED = 4102
    ERROR_REFERENCE_LENGTH_LENGTH_TOO_SMALL = 4103
    ERROR_REFERENCE_NUM_OF_CHANNELS_IS_EXCEEDED = 4104
