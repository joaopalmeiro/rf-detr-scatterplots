# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- Node.js version managers:
  - [nvm](https://github.com/nvm-sh/nvm).
  - [n](https://github.com/tj/n).
- Next.js, being a _full-stack framework_, uses React as its view library.
- React can be seen as a **view library** because, alone, it's not enough to build a modern application — routing, a build system, etc. is needed.
- [Create React App](https://create-react-app.dev/) (CRA): React + build system.
- [Parcel](https://parceljs.org/) (alternative to webpack).
- [When to use Next.js](https://hendrixer.github.io/nextjs-course/what-is-nextjs):
  - All you need is a single-page application (SPA)? Use React/CRA.
  - Do you need a static website, like a blog, which is also a SPA (or something more sophisticated, with SSR, for example)? Use Next.js.
- [`yarn create`](https://classic.yarnpkg.com/en/docs/cli/create/):
  - To create new projects from any `create-*` packages.
  - `yarn create next-app` vs. `npx create-next-app`.
- `yarn add next react react-dom`.
- [Catch all routes](https://nextjs.org/docs/routing/dynamic-routes#catch-all-routes):
  - Dynamic routes can be extended to catch all paths by adding 3 dots inside the brackets (`[...param].jsx`).
  - Think of a glob.
  - [Optional catch all routes](https://nextjs.org/docs/routing/dynamic-routes#optional-catch-all-routes): To include the parent path (`docs/[[...param]].jsx`). This path will correspond to an empty object (`{}`).
- `Link` component (`next/link`): For client-side routing. To link to another website, use the `<a>` tag instead.
- `rsync -ahP --exclude 'node_modules' canvas-react-konva/* /Users/joao.palmeiro/Documents/konva-heatmap` (more info [here](https://blog.duklabs.com/using-rsync-on-mac-to-copy-files/) and [here](https://linuxhint.com/rsync_copy_files/)). The first path is the source, the second one is the destination.
- [auto-changelog](https://github.com/CookPete/auto-changelog) ([npm](https://www.npmjs.com/package/auto-changelog)).
- [Fontsource](https://fontsource.org/) (individual fonts as npm packages).
- [Magic](https://magic.link/) (magic link login/passwordless auth):
  - [How to Implement Auth in Next.js with Magic](https://magic.link/posts/magic-link-nextjs) ([repo](https://github.com/magiclabs/example-nextjs)).
- [Programmatic routing](https://hendrixer.github.io/nextjs-course/navigation#programmatic-routing):
  - The `push` method works like `href` on the `Link` component.
  - To use on buttons, for example.
  - `const router = useRouter()` + `<button onClick={e => router.push('/')}>Go Home</button>`, for example.
- [To apply CSS globally](https://hendrixer.github.io/nextjs-course/styling), you need to create the `pages/_app.jsx` file, the application's entry point, and import the relevant files. If you don't need to apply CSS globally, you don't need to create this file.
- Next.js supports [CSS Modules](https://github.com/css-modules/css-modules) (`*.module.css` files).
- [Theme UI](https://theme-ui.com/):
  - `yarn add theme-ui @theme-ui/presets`.
  - [@theme-ui/presets](https://theme-ui.com/packages/presets/) ([demo](https://theme-ui.com/demo)).
  - [Sketchy Theme UI Preset](https://themeui-sketchy.netlify.app/).
  - The `styles` object is primarily for MDX.
  - `/** @jsx jsx */`: JSX pragma. It is a hint to the compiler (Babel) on how to compile a file. Must be combined with `import { jsx } from 'theme-ui'` (for the same reason you have to import React in JSX files).
  - Alternative: [Base Web](https://baseweb.design/) ([repo](https://github.com/uber/baseweb)).
- In Next.js, we can think of each page as its own application (code splitting).
- [next-react-svg](https://www.npmjs.com/package/next-react-svg) plugin: to transform SVG files to components.
- [next-compose-plugins](https://www.npmjs.com/package/next-compose-plugins) plugin (`yarn add next-compose-plugins`).
- `yarn add next-env dotenv-load --dev`.
- API routes:
  - Create an `api` folder inside the `pages` folder.
- [HTTPie](https://httpie.io/) (CLI for API testing):
  - `brew install httpie`.
  - `http --version`.
  - `http :3000/api` (`:3000` -> `http://localhost:3000/`).
  - [next-connect](https://www.npmjs.com/package/next-connect) package.
  - [Insomnia](https://insomnia.rest/) and [Postman](https://www.postman.com/) (API clients).
- Fetching data:
  - Client-side data fetching packages:
    - [SWR](https://swr.vercel.app/) (React hooks for data fetching).
    - [React Query](https://react-query.tanstack.com/) (and [React Charts](https://react-charts.tanstack.com/)).
  - To fetch data on components (not pages), use client-side data fetching.
  - Next.js injects `fetch` into the environment.
  - To fetch data ahead of time, there are three options (they are for pre-rendered pages only):
    - `getStaticProps`:
      - To fetch data at build time.
      - By having your page exporting `getStaticProps`, Next.js will run this function at build time. The returned props will be passed to the exported page. The results of this function are saved into a JSON file and passed as props to the client's component at runtime.
      - Build time + SSR.
    - `getStaticPaths`:
      - Specify dynamic routes to pre-render pages based on data.
      - To get all the paths to posts from an API or file system, for example.
      - If a page has a dynamic path (`[id].jsx`, for example) and uses `getStaticProps`, it must also use `getStaticPaths`.
      - Use `fallback: true` if you don't want to statically pre-render all pages at once, and instead opt in to render some later at runtime via SSR.
      - Build time + SSR.
    - `getServerSideProps`:
      - By having your page exporting `getServerSideProps`, Next.js will pre-render a page on each request using the data returned by `getServerSideProps`.
      - Do you need data at runtime but don't need SSR? Use client-side data fetching.
      - Do you need data at runtime but do need SSR? Use `getServerSideProps`.
      - Runtime + SSR.
    - More info [here](https://nextjs.org/docs/basic-features/data-fetching).
- [Sheety](https://sheety.co/) (Google Spreadsheets as APIs).
- [Environment Variables](https://nextjs.org/docs/basic-features/environment-variables):
  - Use `.env.local` to load environment variables.
  - Expose environment variables to the browser by prefixing with `NEXT_PUBLIC_`.
- [Slapdash](https://slapdash.com/).
- Rule of thumb: Any non-user generated content should be statically generated.
- Next.js supports dynamic imports (`import dynamic from 'next/dynamic'`) that, when used with components, will opt out of SSR. More info [here](https://hendrixer.github.io/nextjs-course/working-with-ssr). It is possible to add/associate a [loading component](https://nextjs.org/docs/advanced-features/dynamic-import#with-custom-loading-component). In this way, it is possible to have a page only partially pre-rendered.
- https://github.com/browserbase/quickstart-playwright-python-parallelism
- https://blog.adarshd.dev/posts/thread-local-storage-in-python/
  - "Threads share the memory space of their parent process. This will allow us to seamlessly access and share variables, data structures, etc., across threads. But this comes with its own challenges. There may be scenarios where we need to isolate variables and might need to store data specific to each thread. Thread local storage can be leveraged in this case."
  - "We can use `local()` found in the threading module to define thread-local variables."
- https://playwright.dev/python/docs/library#interactive-mode-repl: `playwright = sync_playwright().start()`
- https://playwright.dev/python/docs/library#threading:
  - "Playwright's API is not thread-safe. If you are using Playwright in a multi-threaded environment, you should create a playwright instance per thread."
  - https://github.com/microsoft/playwright-python/issues/623
  - https://github.com/microsoft/playwright-python/issues/470
- https://rfdetr.roboflow.com/latest/learn/train/
  - https://rfdetr.roboflow.com/latest/learn/train/dataset-formats/#coco-format
  - https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/how-to-finetune-rf-detr-on-detection-dataset.ipynb
  - https://universe.roboflow.com/roboflow-jvuqo/basketball-player-detection-2/dataset/13
    - "TRAIN SET 1043 Images"
    - "VALID SET 186 Images"
    - "TEST SET 169 Images"
    - "Resize: Stretch to 640x640"

## Next.js & Netlify Identity (auth) Tutorial

- [#1 Intro & Setup](https://youtu.be/IM7a6BxNof8):
  - [Netlify Identity](https://docs.netlify.com/visitor-access/identity/) documentation.
  - [Netlify Functions](https://docs.netlify.com/functions/overview/) documentation.
- [#2 - Installing Identity & Deploying](https://youtu.be/Pp-wnupZAH4):
  - [netlify-identity-widget](https://www.npmjs.com/package/netlify-identity-widget). Install and deploy the website right after and before using the package. Enable _Identity_ in Netlify interface.
  - [Next.js on Netlify](https://docs.netlify.com/configure-builds/common-configurations/next-js/) documentation. Netlify automatically installs the [Essential Next.js build plugin](https://github.com/netlify/netlify-plugin-nextjs).
- [#3 - Creating an Auth Context](https://youtu.be/WJ8qEkmK0rE):
  - React Context for state management in Next.js.
  - `authReady`: To keep track of when we establish a connection to Netlify because when we load the application, it can take a while to identify whether a user is logged in or not while communicating with Netlify. So until we establish the connection and figure this out, it's going to be `false`.
  - It is possible to have registrations by invitation only. More info [here](https://docs.netlify.com/visitor-access/identity/registration-login/).
- [#4 - Signing Up & Logging In](https://youtu.be/klD6RTbz5ww).
- [#5 - Logging Out](https://youtu.be/Xfr7LIef-q0):
  - Return a function in `useEffect` for cleanup purposes. [React performs the cleanup when the component unmounts](https://reactjs.org/docs/hooks-effect.html#example-using-hooks-1).

## References

- Frontend Masters and Scott Moss' [Introduction to Next.js](https://frontendmasters.com/courses/next-js/) course.
  - [Website](https://hendrixer.github.io/nextjs-course/).
  - [Repo](https://github.com/Hendrixer/nextjs-course-app).

## Development

- `yarn install`.
- `yarn dev`.

## Snippets

### `src/pages/_app.jsx`

```jsx
import { ThemeProvider } from "theme-ui";
import theme from "../../theme";

export default function App({ Component, pageProps }) {
  return (
    <ThemeProvider theme={theme}>
      <Component {...pageProps} />
    </ThemeProvider>
  );
}
```

### `package.json`

```json
{
  "name": "weight",
  "private": true,
  "version": "0.0.1",
  "repository": "https://github.com/joaopalmeiro/weight.git",
  "author": "João Palmeiro <joaommpalmeiro@gmail.com>",
  "license": "MIT",
  "dependencies": {
    "@theme-ui/presets": "^0.10.0",
    "next": "^11.0.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "theme-ui": "^0.10.0"
  },
  "scripts": {
    "dev": "next",
    "build": "next build",
    "start": "next start"
  }
}
```

### `theme.js`

```js
import { roboto } from "@theme-ui/presets";

const theme = {
  ...roboto,
  styles: {
    ...roboto.styles,
  },
};

// console.log(theme);

export default theme;
```
