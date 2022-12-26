export interface GoodsSchema {
    name: string,
    price: number,
    category: {
        name: string
    },
}