export interface UserName {
    username: string
};


export interface CreateUser extends UserName {
    password: string;
};


export interface User extends CreateUser {
    id: number
};


export interface Scope extends CreateUser {
    scope: string
};


export interface UserId extends UserName {
    id: number
};