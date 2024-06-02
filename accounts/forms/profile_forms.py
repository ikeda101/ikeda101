from django import forms
from accounts.models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {"username":    "ユーザー名"
                  ,"department":  "部　　署"
                  ,"phone_number":"電話番号"
                  ,"gender":      "性　　別"
                  ,"birthday":    "生年月日"
                  }
        exclude = ["user"]
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user_email = self.instance.user.email
        if username == user_email:
            raise forms.ValidationError("ユーザー名を変更してください")
        elif "@" in username:
            raise forms.ValidationError("ユーザー名にEメールアドレスは使用できません")
        return username