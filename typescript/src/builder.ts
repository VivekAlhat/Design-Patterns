class User {
  constructor(
    public name: string,
    public age?: number,
    public email?: string
  ) {}
}

interface IUserBuilder {
  setName(name: string): this;
  setAge(age: number): this;
  setEmail(email: string): this;
  build(): User;
}

class UserBuilder implements IUserBuilder {
  private user: Partial<User> = {};

  setName(name: string): this {
    this.user.name = name;
    return this;
  }

  setAge(age: number): this {
    this.user.age = age;
    return this;
  }

  setEmail(email: string): this {
    this.user.email = email;
    return this;
  }

  build(): User {
    if (!this.user.name) {
      throw new Error("User must have a name");
    }

    return new User(this.user.name, this.user.age, this.user.email);
  }
}

const user = new UserBuilder()
  .setName("John Doe")
  .setAge(35)
  .setEmail("johndoe@email.com")
  .build();

console.log(user);

// this will throw an error as user must have a name
// const newUser = new UserBuilder().setAge(70).build();
