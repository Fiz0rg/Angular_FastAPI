export interface GoodsSchema {
    name: string,
    price: number,
    purchases: number,
    category: {
        name: string
    },
}