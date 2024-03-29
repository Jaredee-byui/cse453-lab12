########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Andrew Morris <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

CONTROL_LEVEL = {"Secret": 4,
                "Confidential": 3,
                "Privileged": 2,
                "Public": 1
                }

class Control:
    """
    Confidentiality control following the Bell-LaPadula model
    """

    def __init__(self, text_control: str):
        self._control_access = CONTROL_LEVEL[text_control]

    def security_condition_read(self, user, message) -> bool:
        """
        Checks that the user has access to read the specified asset
        """
        return user >= message

    def security_condition_write(self, user, message) -> bool:
        
        return user <= message


    # def Check_message_visibility(username, message, ):
    #     if access_level == 1:
    #         print(f"Message {message} is available to everyone. ")
    #     elif access_level == 2:
    #         if username == "AdmiralAbe":
    #             print(f"Message {message} is visible to AdmiralAbe. ")
    #         else:
    #             print(f"Message {message} is not  visible to you")
    #     if access_level == 3:
    #             print(f"Message {message} is available to AdmiralAbe")
    #     else:
    #             print(f"Message {message} is not visible to you")
    #     if access_level == 4:
    #         print(f"message {message} is visible to AdmiralAbe")
    #     else:
    #         print(f"message {message} is not visible to you")
        
    # def Check_message_visibility(username, message, access_level):
    #     if access_level == 1:
    #         print(f"Message {message} is available to everyone")
    #     elif access_level == 2:
    #         print(f" Message {message} is not visible  to you")
    #     else:
    #         print(f"message {message} is visible to CaptainCharlie")
    #     if access_level == 3:
    #         print(f"message {message} is not visible to you")
    #     else:
    #         print(f"message {message} is  visible to CaptainCharlie ")
    #     if access_level == "Secret":
    #         print(f"message {message} is not visible to CaptainCharlie")
    #     else:
    #         print(f"message {message} is visible to AdmiralAbe")

    # def Check_message_visibility(username, message, access_level):
    #     if access_level == "public":
    #         print(f"message {message} is visible to everyone")
    #     elif access_level == "Confidential":
    #         print(f"message {message} is visible SeamanSam")
    #     if access_level == 