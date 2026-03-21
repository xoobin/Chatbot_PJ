def calculate_dependency_risk(mirroring_rate):

    if mirroring_rate > 0.7:
        return "HIGH"

    elif mirroring_rate > 0.4:
        return "MEDIUM"

    else:
        return "LOW"