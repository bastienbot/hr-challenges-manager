def normalize_dict(target_dict, default_dict):
    """
    @desc This function sets defaults values for a existing dict
            giving an other dict containing default values.
            This is mostly used to assign a bunch of object props whithout validation

    @params target_dict: dict
    @params default_dict: dict
    @returns default_dict: dict
    """
    for prop, value in default_dict.items():
        target_dict[prop] = target_dict[prop] if prop in target_dict else value
    return target_dict


def format_username(firstname, lastname):
    return "{}.{}.external".format(
        ''.join(e for e in firstname if e.isalnum()),
        ''.join(e for e in lastname if e.isalnum())
    ).lower()
