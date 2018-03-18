
const ENVS = process.env;
const CONTEXT_PATH = ENVS.CONTEXT_PATH;
const ENTRY_NAME = ENVS.ENTRY_NAME;
const ENTRY_PATH = ENVS.ENTRY_PATH;
const DIST_PATH =  ENVS.DIST_PATH;


config = {
    context: CONTEXT_PATH,
    entry: {},
    output: {
        path: DIST_PATH,
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

config.entry[ENTRY_NAME] = ENTRY_PATH;
module.exports = config;
