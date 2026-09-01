import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { headers } from "next/headers";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export async function generateMetadata(): Promise<Metadata> {
  const requestHeaders = await headers();
  const requestedHost = requestHeaders.get("host") ?? "localhost:3000";
  const trustedHost = requestedHost === "localhost:3000" ||
    requestedHost.endsWith(".chatgpt.site") || requestedHost.endsWith(".openai.site");
  const host = trustedHost ? requestedHost : "localhost:3000";
  const base = new URL(`${host.startsWith("localhost") ? "http" : "https"}://${host}`);
  const title = "College Football Daily Moneyline Board";
  const description = "Daily FBS and FCS moneyline opportunities from the 75% market-regressed FPI residual model.";
  return {
    metadataBase: base,
    title,
    description,
    openGraph: {
      title,
      description: "FBS + FCS moneylines, scanned daily. Qualified edges and timing research in one board.",
      images: [{ url: new URL("/og.png", base), width: 1536, height: 1024 }],
    },
    twitter: { card: "summary_large_image", title, description, images: [new URL("/og.png", base)] },
  };
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
