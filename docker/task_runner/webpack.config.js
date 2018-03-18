module.exports = {
    entry: {
        'app': './src/js/app.js',
    },
    output: {
        path: `${__dirname}/dist`,
        filename: "[name].bundle.js"
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.esm.js',
            vuex: 'vuex/dist/vuex.js',
        }
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                options: {
                    presets: [
                        // env を指定することで、ES2017 を ES5 に変換。
                        // {modules: false}にしないと import 文が Babel によって CommonJS に変換され、
                        // webpack の Tree Shaking 機能が使えない
                        ['env', {'modules': false}]
                    ]
                }
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                loader: ['style-loader', 'css-loader'],
            },
            {
                test: /\.vue$/,
                exclude: /node_modules/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                    }
                }
            },
        ]
    },
    devServer: {
        contentBase: 'dist',
        port: 3000,
        host: '0.0.0.0',
        historyApiFallback: true,
    },
};