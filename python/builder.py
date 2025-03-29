class User:
    def __init__(self, name, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"User(name='{self.name}', age={self.age}, email='{self.email}')"


class IUserBuilder:
    def set_name(self, name):
        pass

    def set_age(self, age):
        pass

    def set_email(self, email):
        pass

    def build(self):
        pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.user = {}

    def set_name(self, name):
        self.user["name"] = name
        return self

    def set_age(self, age):
        self.user["age"] = age
        return self

    def set_email(self, email):
        self.user["email"] = email
        return self

    def build(self):
        if "name" not in self.user or not self.user["name"]:
            raise ValueError("User must have a name")

        return User(
            name=self.user.get("name"),
            age=self.user.get("age"),
            email=self.user.get("email"),
        )


# Create a user with the builder
user = (
    UserBuilder()
    .set_name("John Doe")
    .set_age(35)
    .set_email("johndoe@email.com")
    .build()
)

print(user)

# This will throw an error as user must have a name
# new_user = UserBuilder().set_age(70).build()
