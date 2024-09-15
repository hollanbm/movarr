from schema import And, Optional, Use

CONFIG_SCHEMA = {
    "movarr": {
        "name": And(Use(str), lambda string: len(string) > 0),
        Optional(
            "sonarr",
            default=[],
            ignore_extra_keys=True,
        ): And(
            lambda n: len(n),
            [
                {
                    "name": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].name is a required field",
                    ),
                    "enabled": bool,
                    "url": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].url is a required field",
                    ),
                    "destination": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].destination is a required field",
                    ),
                    "api_key": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].api_key is a required field",
                    ),
                    "tag": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].tag is a required field",
                    ),
                }
            ],
            ignore_extra_keys=True,
        ),
        Optional(
            "radarr",
            default=[],
            ignore_extra_keys=True,
        ): And(
            lambda n: len(n),
            [
                {
                    "name": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].name is a required field",
                    ),
                    "enabled": bool,
                    "url": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].url is a required field",
                    ),
                    "destination": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].destination is a required field",
                    ),
                    "api_key": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].api_key is a required field",
                    ),
                    "tag": And(
                        lambda s: s is not None,
                        Use(str),
                        lambda s: len(s) > 0,
                        error="friends[].tag is a required field",
                    ),
                }
            ],
            ignore_extra_keys=True,
        ),
    },
}
