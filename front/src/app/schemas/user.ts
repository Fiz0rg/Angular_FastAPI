export interface UserSchema {
    id: number
    username: string
    is_admin: boolean
}

export interface UserName {
    username: string
};


export interface UsernamePasswordUserSchema extends UserName {
    password: string;
};


export interface User extends UsernamePasswordUserSchema {
    id: number
};


export interface UserId extends UserName {
    id: number
};