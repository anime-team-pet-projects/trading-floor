export type LoginFormType = {
  email: string;
  password: string;
};

export type RegisterFormType = {
  email: string;
  firstName: string;
  lastName?: string;
  password: string;
  roomNumber: number | null;
};
