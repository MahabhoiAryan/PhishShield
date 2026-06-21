def generate_summary(risk, words, urls):

    if risk == "HIGH":

        return (
            "This email appears to be a phishing attempt "
            "because it contains multiple social engineering "
            "indicators and suspicious URLs."
        )

    elif risk == "MEDIUM":

        return (
            "This email contains some suspicious indicators "
            "and should be verified before taking action."
        )

    else:

        return (
            "No significant phishing indicators were detected."
        )