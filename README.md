# Weight, What?

## References

- Frontend Masters and Scott Moss' [Introduction to Next.js](https://frontendmasters.com/courses/next-js/) course.
  - [Website](https://hendrixer.github.io/nextjs-course/).
  - [Repo](https://github.com/Hendrixer/nextjs-course-app).

## Development

- `yarn install`.
- `yarn dev`.

## Notes

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
